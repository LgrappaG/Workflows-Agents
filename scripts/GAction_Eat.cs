using UnityEngine;
using Antigravity.Logic;

namespace Antigravity.AI
{
    [CreateAssetMenu(fileName = "Action_Eat", menuName = "Antigravity/AI/Actions/Eat")]
    public class GAction_Eat : GAction
    {
        public string foodSourceTag = "Food";

        private void OnEnable()
        {
            if (string.IsNullOrEmpty(actionName))
            {
                actionName = "Eat";
                cost = 1f;
                effects.Add(new WorldState { key = "isHungry", value = false });
            }
        }

        public override bool IsPossible(GameObject npc)
        {
            // Logic to check if a food source exists in the scene
            return GameObject.FindGameObjectWithTag(foodSourceTag) != null;
        }

        public override void Perform(GameObject npc)
        {
            Debug.Log($"{npc.name} is looking for food...");

            // Move to food source logic would go here
            var survival = npc.GetComponent<SurvivalHandler>();
            if (survival != null)
            {
                // Rely on the robust, event-driven API created earlier
                survival.RestoreStat(SurvivalHandler.STAT_HUNGER, 100f);
                Debug.Log($"{npc.name} ate and is no longer hungry.");
            }

            // Critical: Release the lock so the NPCBrain can continue
            IsFinished = true;
        }
    }
}
