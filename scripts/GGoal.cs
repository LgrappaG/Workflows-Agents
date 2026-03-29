using UnityEngine;
using System.Collections.Generic;

namespace Antigravity.AI
{
    [CreateAssetMenu(fileName = "NewGoal", menuName = "Antigravity/AI/GOAP Goal")]
    public class GGoal : ScriptableObject
    {
        public string goalName;
        public int priority = 1;

        [Header("Desired World State")]
        public List<GAction.WorldState> desiredState = new List<GAction.WorldState>();
    }
}
