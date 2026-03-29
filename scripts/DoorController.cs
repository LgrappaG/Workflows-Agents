using UnityEngine;

namespace Antigravity.Core.Interaction
{
    /// <summary>
    /// Generic rotatable door interaction controller. Best used on a standalone "Hinge" proxy GameObject.
    /// </summary>
    public class DoorController : MonoBehaviour, IInteractable
    {
        [Header("Door Settings")]
        [SerializeField] private float openAngle = 90f;
        [SerializeField] private float speed = 2f;
        [SerializeField] private Transform doorHinge;

        private bool _isOpen = false;
        private Quaternion _closedRotation;
        private Quaternion _openRotation;
        private Quaternion _targetRotation;

        private void Awake()
        {
            if (doorHinge == null)
            {
                // If no hinge is assigned, assume this object itself is the hinge pivoting point
                doorHinge = transform;
            }

            _closedRotation = doorHinge.localRotation;
            _openRotation = Quaternion.Euler(doorHinge.localEulerAngles + new Vector3(0, openAngle, 0));
            _targetRotation = _closedRotation;
        }

        private void Update()
        {
            if (doorHinge.localRotation != _targetRotation)
            {
                doorHinge.localRotation = Quaternion.Slerp(doorHinge.localRotation, _targetRotation, Time.deltaTime * speed);
            }
        }

        public void Interact()
        {
            _isOpen = !_isOpen;
            _targetRotation = _isOpen ? _openRotation : _closedRotation;
            
            // Optional: Play Sound here
            // Debug.Log(_isOpen ? "Door Opened" : "Door Closed");
        }

        public string GetPrompt()
        {
            return _isOpen ? "Press [E] to Close Door" : "Press [E] to Open Door";
        }
    }
}
