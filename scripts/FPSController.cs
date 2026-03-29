using UnityEngine;
using UnityEngine.InputSystem; // Added InputSystem

namespace Antigravity.Core.Player
{
    /// <summary>
    /// A robust, physics-based First Person Controller utilizing the modern Input System and CharacterController.
    /// Does not require legacy Input Manager setup.
    /// </summary>
    [RequireComponent(typeof(CharacterController))]
    public class FPSController : MonoBehaviour
    {
        [Header("Movement Settings")]
        [SerializeField] private float walkSpeed = 5.0f;
        [SerializeField] private float sprintSpeed = 8.0f;
        [SerializeField] private float jumpHeight = 1.5f;
        [SerializeField] private float gravity = -9.81f;

        [Header("Look Settings")]
        [SerializeField] private Transform playerCamera;
        [SerializeField] private float mouseSensitivity = 0.1f; // Usually needs to be much lower for new Input System
        [SerializeField] private float upDownRange = 85.0f;

        private CharacterController _characterController;
        private Vector3 _velocity;
        private float _verticalRotation;
        private bool _isGrounded;

        // Input Action references
        private InputAction _moveAction;
        private InputAction _lookAction;
        private InputAction _jumpAction;
        private InputAction _sprintAction;

        private void Awake()
        {
            _characterController = GetComponent<CharacterController>();
            
            Cursor.lockState = CursorLockMode.Locked;
            Cursor.visible = false;
            
            if (playerCamera == null)
            {
                playerCamera = GetComponentInChildren<Camera>().transform;
            }

            SetupInput();
        }

        private void SetupInput()
        {
            // Instead of requiring an Input Actions Asset for this prototype, we'll create actions in memory
            _moveAction = new InputAction("Move", binding: "<Gamepad>/leftStick");
            _moveAction.AddCompositeBinding("Dpad")
                .With("Up", "<Keyboard>/w")
                .With("Down", "<Keyboard>/s")
                .With("Left", "<Keyboard>/a")
                .With("Right", "<Keyboard>/d");

            _lookAction = new InputAction("Look", binding: "<Gamepad>/rightStick");
            _lookAction.AddBinding("<Pointer>/delta");

            _jumpAction = new InputAction("Jump", binding: "<Keyboard>/space");
            _jumpAction.AddBinding("<Gamepad>/buttonSouth");

            _sprintAction = new InputAction("Sprint", binding: "<Keyboard>/leftShift");
            _sprintAction.AddBinding("<Gamepad>/leftStickPress");
        }

        private void OnEnable()
        {
            _moveAction.Enable();
            _lookAction.Enable();
            _jumpAction.Enable();
            _sprintAction.Enable();

            _jumpAction.performed += OnJump;
        }

        private void OnDisable()
        {
            _moveAction.Disable();
            _lookAction.Disable();
            _jumpAction.Disable();
            _sprintAction.Disable();

            _jumpAction.performed -= OnJump;
        }

        private void Update()
        {
            HandleLook();
            HandleMovement();
        }

        private void HandleLook()
        {
            if (playerCamera == null) return;

            Vector2 lookInput = _lookAction.ReadValue<Vector2>();
            float mouseX = lookInput.x * mouseSensitivity;
            float mouseY = lookInput.y * mouseSensitivity;

            // Rotate Player horizontally (Y-axis)
            transform.Rotate(0, mouseX, 0);

            // Rotate Camera vertically (X-axis) with clamping
            _verticalRotation -= mouseY;
            _verticalRotation = Mathf.Clamp(_verticalRotation, -upDownRange, upDownRange);
            playerCamera.localRotation = Quaternion.Euler(_verticalRotation, 0, 0);
        }

        private void HandleMovement()
        {
            _isGrounded = _characterController.isGrounded;
            if (_isGrounded && _velocity.y < 0)
            {
                _velocity.y = -2f;
            }

            Vector2 moveInput = _moveAction.ReadValue<Vector2>();

            // Calculate movement direction relative to player's facing direction
            Vector3 move = transform.right * moveInput.x + transform.forward * moveInput.y;

            float currentSpeed = _sprintAction.IsPressed() ? sprintSpeed : walkSpeed;
            
            _characterController.Move(move * (currentSpeed * Time.deltaTime));

            // Apply gravity
            _velocity.y += gravity * Time.deltaTime;
            _characterController.Move(_velocity * Time.deltaTime);
        }

        private void OnJump(InputAction.CallbackContext context)
        {
            if (_isGrounded)
            {
                _velocity.y = Mathf.Sqrt(jumpHeight * -2f * gravity);
            }
        }
    }
}
