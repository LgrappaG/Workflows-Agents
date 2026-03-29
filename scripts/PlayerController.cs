using UnityEngine;
using UnityEngine.InputSystem;
using UnityEngine.UI;
using Antigravity.Logic;

namespace Antigravity.Utilities
{
    /// <summary>
    /// A robust, physics-based (Rigidbody) First Person controller.
    /// Handles movement, jumping, smooth look rotation, and interactive raycasts.
    /// Utilizes the new Unity Input System via direct InputAction bindings.
    /// </summary>
    [RequireComponent(typeof(Rigidbody), typeof(CapsuleCollider))]
    public class PlayerController : MonoBehaviour
    {
        [Header("Movement")]
        public float walkSpeed = 5f;
        public float lookSpeed = 1.5f; // Increased default for smoother feel
        public float groundDrag = 5f;
        public float jumpForce = 7f;

        [Header("Ground Check")]
        public float playerHeight = 2f;
        public LayerMask groundLayer;
        private bool _isGrounded;
        [Header("Interaction")]
        public float interactRange = 3f;
        public LayerMask interactLayer;
        public GameObject interactionHintUI; // The "Press E" text object

        [Header("References")]
        public Transform cameraTransform;

        private Rigidbody _rb;
        private float _rotationX = 0;
        private Vector2 _moveInput;
        private Vector2 _lookInput;

        // Input Actions
        private InputAction _moveAction;
        private InputAction _lookAction;
        private InputAction _jumpAction;
        private InputAction _interactAction;

        private void Awake()
        {
            _rb = GetComponent<Rigidbody>();
            _rb.freezeRotation = true;
            _rb.linearDamping = groundDrag;

            if (cameraTransform == null) cameraTransform = GetComponentInChildren<Camera>()?.transform;

            // Lock cursor
            Cursor.lockState = CursorLockMode.Locked;
            Cursor.visible = false;

            if (interactionHintUI != null) interactionHintUI.SetActive(false);

            SetupInputActions();
        }

        private void SetupInputActions()
        {
            // Create and bind Input Actions directly (avoiding the need for an external Asset for this component)
            _moveAction = new InputAction("Move", binding: "<Gamepad>/leftStick");
            _moveAction.AddCompositeBinding("Dpad")
                .With("Up", "<Keyboard>/w")
                .With("Down", "<Keyboard>/s")
                .With("Left", "<Keyboard>/a")
                .With("Right", "<Keyboard>/d");

            _lookAction = new InputAction("Look", binding: "<Pointer>/delta");

            _jumpAction = new InputAction("Jump", binding: "<Keyboard>/space");
            _jumpAction.AddBinding("<Gamepad>/buttonSouth");

            _interactAction = new InputAction("Interact", binding: "<Keyboard>/e");
            _interactAction.AddBinding("<Mouse>/leftButton");
            _interactAction.AddBinding("<Gamepad>/buttonWest");

            // Subscribe to discrete events
            _jumpAction.performed += ctx => { if (_isGrounded) Jump(); };
            _interactAction.performed += ctx => HandleInteraction();
        }

        private void OnEnable()
        {
            _moveAction?.Enable();
            _lookAction?.Enable();
            _jumpAction?.Enable();
            _interactAction?.Enable();
        }

        private void OnDisable()
        {
            _moveAction?.Disable();
            _lookAction?.Disable();
            _jumpAction?.Disable();
            _interactAction?.Disable();
        }

        private void Update()
        {
            // Read continuous inputs
            _moveInput = _moveAction.ReadValue<Vector2>();
            _lookInput = _lookAction.ReadValue<Vector2>() * 0.1f; // Scale down raw input for smoother feel

            HandleRotation();
            CheckInteractionHint();

            // Ground Check (SphereCast is more reliable than Raycast)
            _isGrounded = Physics.SphereCast(transform.position, 0.4f, Vector3.down, out RaycastHit hit, (playerHeight * 0.5f) - 0.3f, groundLayer);
        }

        private void Jump()
        {
            // Reset y velocity before jumping to ensure consistent jump height 
            _rb.linearVelocity = new Vector3(_rb.linearVelocity.x, 0f, _rb.linearVelocity.z);
            _rb.AddForce(transform.up * jumpForce, ForceMode.Impulse);
        }

        private void FixedUpdate()
        {
            HandleMovement();
        }

        private void HandleMovement()
        {
            Vector3 targetVelocity = (transform.forward * _moveInput.y + transform.right * _moveInput.x).normalized * walkSpeed;

            // Calculate velocity change needed to reach target velocity
            Vector3 currentVelocity = _rb.linearVelocity;
            Vector3 velocityChange = (targetVelocity - currentVelocity);

            // Do not apply force on the Y axis to let gravity and jump handle it
            velocityChange.y = 0;

            _rb.AddForce(velocityChange, ForceMode.VelocityChange);
        }

        private void HandleRotation()
        {
            // Smooth horizontal rotation (Body)
            transform.Rotate(Vector3.up * _lookInput.x * lookSpeed);

            // Smooth vertical rotation (Camera)
            _rotationX -= _lookInput.y * lookSpeed;
            _rotationX = Mathf.Clamp(_rotationX, -90f, 90f);
            cameraTransform.localRotation = Quaternion.Euler(_rotationX, 0, 0);
        }

        private void CheckInteractionHint()
        {
            if (interactionHintUI == null) return;

            Ray ray = new Ray(cameraTransform.position, cameraTransform.forward);
            bool hittingInteractable = false;

            if (Physics.Raycast(ray, out RaycastHit hit, interactRange, interactLayer))
            {
                if (hit.collider.GetComponent<SurvivalRestorer>() != null)
                {
                    hittingInteractable = true;
                }
            }

            if (interactionHintUI.activeSelf != hittingInteractable)
            {
                interactionHintUI.SetActive(hittingInteractable);
            }
        }

        private void HandleInteraction()
        {
            Ray ray = new Ray(cameraTransform.position, cameraTransform.forward);
            if (Physics.Raycast(ray, out RaycastHit hit, interactRange, interactLayer))
            {
                var restorer = hit.collider.GetComponent<SurvivalRestorer>();
                if (restorer != null)
                {
                    restorer.Restore();
                }
            }
        }
    }
}
