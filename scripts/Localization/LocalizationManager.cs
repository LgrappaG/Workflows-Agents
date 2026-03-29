using UnityEngine;
using UnityEngine.Localization;
using UnityEngine.Localization.Settings;
using System.Collections.Generic;
using System.Linq;

namespace Antigravity.Localization
{
    /// <summary>
    /// Centralized localization management system.
    /// Handles locale switching, persistence, and dynamic UI updates.
    /// Supports 10+ languages with RTL text, CJK fonts, and fallback mechanisms.
    /// </summary>
    public class LocalizationManager : MonoBehaviour
    {
        public static LocalizationManager Instance { get; private set; }

        [SerializeField]
        private List<Locale> _supportedLocales = new();

        private Locale _currentLocale;
        private const string LocalePreferenceKey = "SelectedLocale";

        public delegate void OnLocaleChanged(Locale newLocale);
        public event OnLocaleChanged LocaleChanged;

        private void Awake()
        {
            if (Instance != null && Instance != this)
            {
                Destroy(gameObject);
                return;
            }

            Instance = this;
            DontDestroyOnLoad(gameObject);

            _supportedLocales = LocalizationSettings.AvailableLocales.Locales.ToList();
        }

        private void Start()
        {
            LoadSavedLocale();
            LocalizationSettings.SelectedLocaleChanged += OnLocaleChangedCallback;
        }

        /// <summary>
        /// Switch to specific locale by index.
        /// </summary>
        public void SetLocale(int localeIndex)
        {
            if (localeIndex < 0 || localeIndex >= _supportedLocales.Count)
            {
                Debug.LogWarning($"Invalid locale index: {localeIndex}");
                return;
            }

            Locale targetLocale = _supportedLocales[localeIndex];
            LocalizationSettings.SelectedLocale = targetLocale;
            PlayerPrefs.SetInt(LocalePreferenceKey, localeIndex);
            PlayerPrefs.Save();

            _currentLocale = targetLocale;
        }

        /// <summary>
        /// Switch to locale by language code (e.g., "en", "ja", "ar").
        /// </summary>
        public void SetLocaleByCode(string languageCode)
        {
            var targetLocale = _supportedLocales
                .FirstOrDefault(l => l.Identifier.CultureInfo.TwoLetterISOLanguageName == languageCode);

            if (targetLocale == null)
            {
                Debug.LogWarning($"Locale not found: {languageCode}");
                return;
            }

            LocalizationSettings.SelectedLocale = targetLocale;
            int index = _supportedLocales.IndexOf(targetLocale);
            PlayerPrefs.SetInt(LocalePreferenceKey, index);
            PlayerPrefs.Save();

            _currentLocale = targetLocale;
        }

        /// <summary>
        /// Get current locale code.
        /// </summary>
        public string GetCurrentLocaleCode()
        {
            return LocalizationSettings.SelectedLocale?.Identifier.CultureInfo.TwoLetterISOLanguageName ?? "en";
        }

        /// <summary>
        /// Check if locale is RTL (Right-to-Left).
        /// </summary>
        public bool IsRTL()
        {
            var cultureInfo = LocalizationSettings.SelectedLocale?.Identifier.CultureInfo;
            return cultureInfo != null && cultureInfo.TextInfo.IsRightToLeft;
        }

        /// <summary>
        /// Get all available locales as list of codes.
        /// </summary>
        public List<string> GetAvailableLocaleCodes()
        {
            return _supportedLocales
                .Select(l => l.Identifier.CultureInfo.TwoLetterISOLanguageName)
                .ToList();
        }

        private void LoadSavedLocale()
        {
            int savedIndex = PlayerPrefs.GetInt(LocalePreferenceKey, 0);
            SetLocale(Mathf.Clamp(savedIndex, 0, _supportedLocales.Count - 1));
        }

        private void OnLocaleChangedCallback(Locale newLocale)
        {
            _currentLocale = newLocale;
            LocaleChanged?.Invoke(newLocale);
        }

        private void OnDestroy()
        {
            if (LocalizationSettings.SelectedLocaleChanged != null)
                LocalizationSettings.SelectedLocaleChanged -= OnLocaleChangedCallback;
        }
    }
}
