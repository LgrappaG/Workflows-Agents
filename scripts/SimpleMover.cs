using UnityEngine;
using UnityEngine.InputSystem;

namespace Antigravity.Utilities
{
    public class SimpleMover : MonoBehaviour
    {
        private float rotationX = 0f;
        public float speed = 5f;
        public float lookSpeed = 0.5f;

        private InputAction _moveAction;
        private InputAction _lookAction;
        private InputAction _rotateAction;

        private void Awake()
        {
            _moveAction = new InputAction("Move");
            _moveAction.AddCompositeBinding("Dpad")
                .With("Up", "<Keyboard>/w")
                .With("Down", "<Keyboard>/s")
                .With("Left", "<Keyboard>/a")
                .With("Right", "<Keyboard>/d");

            _lookAction = new InputAction("Look", binding: "<Mouse>/delta");
            _rotateAction = new InputAction("Rotate", type: InputActionType.Button, binding: "<Mouse>/rightButton");
        }

        private void OnEnable()
        {
            _moveAction.Enable();
            _lookAction.Enable();
            _rotateAction.Enable();
        }

        private void OnDisable()
        {
            _moveAction.Disable();
            _lookAction.Disable();
            _rotateAction.Disable();
        }

        void Update()
        {
            // Movement
            Vector2 moveInput = _moveAction.ReadValue<Vector2>();
            Vector3 move = new Vector3(moveInput.x, 0, moveInput.y);
            transform.Translate(move * speed * Time.deltaTime, Space.Self);

            // Rotation
            if (_rotateAction.ReadValue<float>() > 0)
            {
                var delta = _lookAction.ReadValue<Vector2>();

                rotationX += -delta.y * lookSpeed;
                rotationX = Mathf.Clamp(rotationX, -90f, 90f);
                float rotationY = delta.x * lookSpeed;

                transform.Rotate(Vector3.up, rotationY, Space.World);
                var angles = transform.localEulerAngles;
                angles.x = rotationX;
                transform.localEulerAngles = angles;
            }
        }
    }
}
