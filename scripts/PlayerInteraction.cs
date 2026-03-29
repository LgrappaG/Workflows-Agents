using UnityEngine;
using UnityEngine.InputSystem;

namespace Antigravity.Core.Interaction
{
    /// <summary>
    /// Handles central raycasting logic for detecting and interacting with IInteractable objects.
    /// Automatically manages input and UI prompt rendering.
    /// </summary>
    public class PlayerInteraction : MonoBehaviour
    {
        [Header("Interaction Settings")]
        [SerializeField] private float interactRange = 3f;
        // Check all layers by default so we don't need to manually setup layers in the Editor
        [SerializeField] private LayerMask interactableLayer = ~0; 
        [SerializeField] private Camera playerCamera;

        [Header("UI Feedback")]
        [SerializeField] private bool showPromptInGUI = true;

        private IInteractable _currentInteractable;
        private InputAction _interactAction;

        private void Awake()
        {
            if (playerCamera == null)
            {
                playerCamera = GetComponentInChildren<Camera>();
            }

            _interactAction = new InputAction("Interact", binding: "<Keyboard>/e");
            _interactAction.AddBinding("<Gamepad>/buttonWest");
        }

        private void OnEnable()
        {
            _interactAction.Enable();
            _interactAction.performed += OnInteract;
        }

        private void OnDisable()
        {
            _interactAction.Disable();
            _interactAction.performed -= OnInteract;
        }

        private void Update()
        {
            HandleInteractionRaycast();
        }

        private void HandleInteractionRaycast()
        {
            if (playerCamera == null) return;

            Ray ray = playerCamera.ViewportPointToRay(new Vector3(0.5f, 0.5f, 0));
            
            if (Physics.Raycast(ray, out RaycastHit hitInfo, interactRange, interactableLayer))
            {
                // To avoid errors, we first check if the object we hit has the IInteractable component.
                // Note: The DoorVisual is a child of the DoorHinge. The collider is on the Visual, 
                // but the script is on the Hinge. We use GetComponentInParent to find it!
                _currentInteractable = hitInfo.collider.GetComponentInParent<IInteractable>();
            }
            else
            {
                _currentInteractable = null;
            }
        }

        private void OnInteract(InputAction.CallbackContext context)
        {
            if (_currentInteractable != null)
            {
                _currentInteractable.Interact();
            }
        }

        private void OnGUI()
        {
            if (!showPromptInGUI) return;

            if (_currentInteractable != null)
            {
                string prompt = _currentInteractable.GetPrompt();
                
                GUI.color = Color.white;
                GUI.Label(new Rect(Screen.width / 2 - 10, Screen.height / 2 - 10, 20, 20), "+");
                
                GUIStyle style = new GUIStyle();
                style.alignment = TextAnchor.MiddleCenter;
                style.normal.textColor = Color.yellow;
                style.fontSize = 20;
                
                GUI.Label(new Rect(0, Screen.height / 2 + 20, Screen.width, 40), prompt, style);
            }
            else
            {
                GUI.color = new Color(1, 1, 1, 0.5f);
                GUI.Label(new Rect(Screen.width / 2 - 10, Screen.height / 2 - 10, 20, 20), "+");
            }
        }
    }
}
