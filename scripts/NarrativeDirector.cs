using UnityEngine;
using UnityEngine.Events;

namespace Antigravity.Narrative
{
    /// <summary>
    /// Manages the high-level flow of the story, transitioning between gameplay states.
    /// </summary>
    public class NarrativeDirector : MonoBehaviour
    {
        public enum NarrativeState
        {
            FreeRoam,
            Dialogue,
            Cinematic,
            Paused
        }

        [Header("Current Status")]
        public NarrativeState currentState = NarrativeState.FreeRoam;

        [Header("State Events")]
        public UnityEvent OnDialogueStart;
        public UnityEvent OnDialogueEnd;
        public UnityEvent OnCinematicStart;
        public UnityEvent OnCinematicEnd;

        private static NarrativeDirector _instance;
        public static NarrativeDirector Instance => _instance;

        private void Awake()
        {
            if (_instance == null) _instance = this;
            else Destroy(gameObject);
        }

        public void SetState(NarrativeState newState)
        {
            if (currentState == newState) return;

            // Exit logic for old state
            ExitState(currentState);

            // Enter logic for new state
            currentState = newState;
            EnterState(currentState);
        }

        private void EnterState(NarrativeState state)
        {
            switch (state)
            {
                case NarrativeState.Dialogue:
                    OnDialogueStart?.Invoke();
                    LockPlayerInput(true);
                    break;
                case NarrativeState.Cinematic:
                    OnCinematicStart?.Invoke();
                    LockPlayerInput(true);
                    break;
                case NarrativeState.FreeRoam:
                    LockPlayerInput(false);
                    break;
            }
        }

        private void ExitState(NarrativeState state)
        {
            switch (state)
            {
                case NarrativeState.Dialogue:
                    OnDialogueEnd?.Invoke();
                    break;
                case NarrativeState.Cinematic:
                    OnCinematicEnd?.Invoke();
                    break;
            }
        }

        private void LockPlayerInput(bool locked)
        {
            // This would integrate with your specific CharacterController or InputSystem
            Debug.Log($"[NarrativeDirector] Player Input Locked: {locked}");

            // Example: Cursor visibility
            if (locked)
            {
                Cursor.lockState = CursorLockMode.None;
                Cursor.visible = true;
            }
            else
            {
                Cursor.lockState = CursorLockMode.Locked;
                Cursor.visible = false;
            }
        }

        // Methods to be called by Yarn Spinner or Triggers
        public void StartDialogue() => SetState(NarrativeState.Dialogue);
        public void EndDialogue() => SetState(NarrativeState.FreeRoam);
        public void StartCinematic() => SetState(NarrativeState.Cinematic);
        public void EndCinematic() => SetState(NarrativeState.FreeRoam);
    }
}
