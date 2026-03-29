using UnityEngine;
using System.Collections.Generic;

namespace Antigravity.AI
{
    /// <summary>
    /// Base class for all NPC actions in the GOAP system.
    /// MCP can generate child classes or configure instances of this to define behaviors.
    /// </summary>
    public abstract class GAction : ScriptableObject
    {
        public string actionName;
        public float cost = 1.0f;
        public string animationTrigger;

        [HideInInspector]
        public bool IsFinished { get; protected set; } = false;

        [Header("World State Requirements")]
        public List<WorldState> preconditions = new List<WorldState>();
        public List<WorldState> effects = new List<WorldState>();

        [System.Serializable]
        public struct WorldState
        {
            public string key;
            public bool value;
        }

        /// <summary>
        /// Logic to determine if the action is physically possible in the scene.
        /// </summary>
        public abstract bool IsPossible(GameObject npc);

        /// <summary>
        /// Execution logic for the action. Custom logic should set IsFinished to true when complete.
        /// </summary>
        public abstract void Perform(GameObject npc);

        /// <summary>
        /// Resets the action state so it can be re-queued in future plans.
        /// </summary>
        public virtual void ResetAction()
        {
            IsFinished = false;
        }
    }
}
