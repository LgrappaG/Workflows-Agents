using UnityEngine;

namespace Antigravity.Core.Interaction
{
    /// <summary>
    /// Generic sliding drawer/cabinet intersection controller.
    /// </summary>
    public class CabinetController : MonoBehaviour, IInteractable
    {
        [Header("Cabinet Settings")]
        [SerializeField] private float slideDistance = 0.5f;
        [SerializeField] private float speed = 3f;
        [SerializeField] private bool slideForward = true;

        private bool _isOpen = false;
        private Vector3 _closedPosition;
        private Vector3 _openPosition;
        private Vector3 _targetPosition;

        private void Awake()
        {
            _closedPosition = transform.localPosition;
            
            // Determine the open location based on Local Z-axis (forward) or whatever is suitable
            Vector3 direction = slideForward ? transform.forward : transform.right; // Example based on world space for simplicity, but can be local
            
            _openPosition = transform.position + (transform.forward * slideDistance);
            _targetPosition = transform.position; // start closed
        }

        private void Update()
        {
            if (transform.position != _targetPosition)
            {
                transform.position = Vector3.Lerp(transform.position, _targetPosition, Time.deltaTime * speed);
            }
        }

        public void Interact()
        {
            _isOpen = !_isOpen;
            _targetPosition = _isOpen ? _openPosition : _closedPosition;
        }

        public string GetPrompt()
        {
            return _isOpen ? "Press [E] to Close Cabinet" : "Press [E] to Open Cabinet";
        }
    }
}
