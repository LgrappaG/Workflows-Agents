using UnityEngine;
using System.Collections.Generic;

namespace Antigravity.AI
{
    /// <summary>
    /// The master controller for an intelligent NPC.
    /// Manages goals, planning, and execution loops.
    /// </summary>
    public class NPCBrain : MonoBehaviour
    {
        public List<GGoal> goals = new List<GGoal>();
        public GPlanner planner;

        private Queue<GAction> _actionQueue;
        private GAction _currentAction;
        private Dictionary<string, bool> _worldState = new Dictionary<string, bool>();

        private void Start()
        {
            if (planner == null) planner = GetComponent<GPlanner>();
            InvokeRepeating(nameof(RefreshPlan), 0f, 2f);
        }

        private void RefreshPlan()
        {
            if (goals.Count == 0) return;

            // Pick highest priority goal
            GGoal topGoal = goals[0]; // Simplified for scaffold
            _actionQueue = planner.Plan(topGoal, _worldState);
        }

        private void Update()
        {
            if (_currentAction == null && (_actionQueue == null || _actionQueue.Count == 0)) return;

            if (_currentAction == null)
            {
                _currentAction = _actionQueue.Dequeue();
                if (_currentAction.IsPossible(gameObject))
                {
                    _currentAction.ResetAction();
                    _currentAction.Perform(gameObject);
                }
                else
                {
                    _currentAction = null; // Re-plan needed
                }
            }
            else if (_currentAction != null)
            {
                // Wait for completion, assuming Perform manages its own internal state and sets IsFinished to true eventually.
                if (_currentAction.IsFinished)
                {
                    _currentAction = null; // Grab next in queue on next frame
                }
            }
        }
    }
}
