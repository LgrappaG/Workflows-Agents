using UnityEngine;

namespace Antigravity.AI
{
    [CreateAssetMenu(fileName = "Action_Socialize", menuName = "Antigravity/AI/Actions/Socialize")]
    public class GAction_Socialize : GAction
    {
        private POITag _targetPOI;

        private void OnEnable()
        {
            if (string.IsNullOrEmpty(actionName))
            {
                actionName = "Socialize";
                cost = 2f; // Socializing takes more 'effort' than eating
                effects.Add(new WorldState { key = "isLonely", value = false });
            }
        }

        public override bool IsPossible(GameObject npc)
        {
            if (SocialManager.Instance == null) return false;

            _targetPOI = SocialManager.Instance.FindNearestPOI(npc.transform.position, POITag.POIType.Social);
            return _targetPOI != null;
        }

        public override void Perform(GameObject npc)
        {
            if (_targetPOI == null)
            {
                IsFinished = true;
                return;
            }

            Debug.Log($"{npc.name} is heading to {_targetPOI.name} to socialize.");

            // Logic to move to _targetPOI.transform.position
            _targetPOI.RegisterUser();

            // Simplified logic: After some time or event, unregister.
            // For now, mark as finished immediately so brain doesn't hang.
            IsFinished = true;
        }
    }
}
