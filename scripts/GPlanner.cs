using UnityEngine;
using System.Collections.Generic;
using System.Linq;

namespace Antigravity.AI
{
    /// <summary>
    /// Calculates the sequence of actions needed to satisfy an NPC's goal.
    /// </summary>
    public class GPlanner : MonoBehaviour
    {
        public List<GAction> allActions = new List<GAction>();

        public Queue<GAction> Plan(GGoal goal, Dictionary<string, bool> worldState)
        {
            List<GAction> usableActions = allActions.Where(a => a != null).ToList();

            GNode startNode = new GNode(null, 0, worldState, null);
            List<GNode> leaves = new List<GNode>();

            if (BuildGraph(startNode, leaves, usableActions, goal.desiredState))
            {
                GNode cheapest = null;
                foreach (var leaf in leaves)
                {
                    if (cheapest == null || leaf.runningCost < cheapest.runningCost)
                    {
                        cheapest = leaf;
                    }
                }

                List<GAction> result = new List<GAction>();
                GNode current = cheapest;
                while (current != null)
                {
                    if (current.action != null) result.Insert(0, current.action);
                    current = current.parent;
                }

                return new Queue<GAction>(result);
            }

            Debug.LogWarning("[GPlanner] Failed to find a valid plan for goal: " + goal.goalName);
            return null;
        }

        private bool BuildGraph(GNode parent, List<GNode> leaves, List<GAction> actions, List<GAction.WorldState> goalState)
        {
            bool foundPath = false;

            foreach (var action in actions)
            {
                if (InState(action.preconditions, parent.state))
                {
                    Dictionary<string, bool> currentState = new Dictionary<string, bool>(parent.state);
                    foreach (var effect in action.effects)
                    {
                        currentState[effect.key] = effect.value;
                    }

                    GNode node = new GNode(parent, parent.runningCost + action.cost, currentState, action);

                    if (InState(goalState, currentState))
                    {
                        leaves.Add(node);
                        foundPath = true;
                    }
                    else
                    {
                        List<GAction> subset = new List<GAction>(actions);
                        subset.Remove(action);
                        if (BuildGraph(node, leaves, subset, goalState)) foundPath = true;
                    }
                }
            }

            return foundPath;
        }

        private bool InState(List<GAction.WorldState> test, Dictionary<string, bool> state)
        {
            foreach (var t in test)
            {
                if (!state.ContainsKey(t.key) || state[t.key] != t.value) return false;
            }
            return true;
        }
    }

    public class GNode
    {
        public GNode parent;
        public float runningCost;
        public Dictionary<string, bool> state;
        public GAction action;

        public GNode(GNode parent, float cost, Dictionary<string, bool> state, GAction action)
        {
            this.parent = parent;
            this.runningCost = cost;
            this.state = state;
            this.action = action;
        }
    }
}
