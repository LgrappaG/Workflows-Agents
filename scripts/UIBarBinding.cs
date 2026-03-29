using UnityEngine;
using UnityEngine.UI;
using Antigravity.Logic;

namespace Antigravity.UI
{
    /// <summary>
    /// Automatically binds a UI Image (as a progress bar) to a SurvivalHandler stat.
    /// MCP can use this to setup HUDs instantly.
    /// </summary>
    public class UIBarBinding : MonoBehaviour
    {
        public string statToFollow = SurvivalHandler.STAT_HUNGER;
        public Image fillImage;
        public float smoothSpeed = 5f;

        private SurvivalHandler _handler;
        private float _targetFillAmount;

        private void Start()
        {
            _handler = Object.FindFirstObjectByType<SurvivalHandler>();
            if (fillImage == null) fillImage = GetComponent<Image>();

            if (_handler != null)
            {
                _handler.OnStatChanged += HandleStatChanged;
                // Initial set
                _targetFillAmount = _handler.GetStatNormalized(statToFollow);
                fillImage.fillAmount = _targetFillAmount;
            }
        }

        private void OnDestroy()
        {
            if (_handler != null)
            {
                _handler.OnStatChanged -= HandleStatChanged;
            }
        }

        private void HandleStatChanged(string statName, float normalizedValue)
        {
            if (statName == statToFollow)
            {
                _targetFillAmount = normalizedValue;
            }
        }

        private void Update()
        {
            if (fillImage != null && Mathf.Abs(fillImage.fillAmount - _targetFillAmount) > 0.001f)
            {
                fillImage.fillAmount = Mathf.Lerp(fillImage.fillAmount, _targetFillAmount, Time.deltaTime * smoothSpeed);
            }
        }
    }
}
