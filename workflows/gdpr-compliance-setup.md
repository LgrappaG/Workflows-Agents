---
version: 9.0.0
category: Accessibility & Compliance
agent: Accessibility Expert
difficulty: beginner
estimated_time: 1-2 hours
skills:
  required:
  - networking-server-security
  - analytics-integration
  - data-pipeline-setup
  - custom-workflow-builder
  - networking-ngo-setup
  - animation-mocap-setup
  - machine-learning-setup
  - godot-animation-setup
  - networking-guild-system
  - ui-form-submission
  - ui-accessibility
  - ui-focus-navigation
  - ui-keyboard-shortcuts
  - animation-baking-setup
  - animation-humanoid-setup
  - animation-ik-setup
  - animation-mirror-setup
  - audio-mixer-setup
  - ci-cd-pipeline-setup
  - godot-setup
  - graphics-hdrp-setup
  - graphics-lightmap-setup
  - graphics-urp-setup
  - material-pbr-setup
  - material-translucency-setup
  - navmesh-baking-setup
  - physics-vehicle-setup
  - ui-two-way-binding
  - ui-context-menus
  - ui-tooltips
  - ai-debugging-tools
  - debug-build-diagnostic
  - material-metallic-workflow
  - material-specular-workflow
  - ui-data-binding
  - ui-drag-drop
  - ui-event-handlers
  - ui-input-validation
  - ui-list-repeater
  - ui-modal-dialogs
  - ui-panel-layout
  - ui-prefab-variants
  - ui-text-binding
  - build-system-optimization
  - csharp-builder-pattern
  - engine-migration-guide
  - material-disney-workflow
  - networking-lobby-system
  - networking-reward-distribution
  - networking-server-maintenance
  - physics-fluid-dynamics
  - privacy-preservation
  - ui-anchor-positioning
  - ui-animation-states
  - ui-animation-tweens
  - ui-auto-layout
  - ui-button-events
  - ui-docking-windows
  - ui-dynamic-styling
  - ui-grid-layout
  - ui-hierarchy-panel
  - ui-list-virtualization
  - ui-mouse-interaction
  - ui-overflow-handling
  - ui-performance-optimization
  - ui-resize-scaling
  - ui-responsive-design
  - ui-scrolling-behavior
  - ui-style-sheets
  - ui-theme-switching
  - ui-touch-input
  - ui-transition-timing
  - ui-visual-feedback
  - ui-z-ordering
  - vfx-builtin-particles
  - networking-achievement-tracking
  - networking-analytics-tracking
  - networking-cloud-saves
  - networking-encryption
  - networking-replay-system
  - networking-server-authority
  - ai-learning-adaptation
  - ai-perception-system
  - animation-constraint-rigging
  - csharp-chain-of-responsibility
  recommended:
  - networking-authentication
  - networking-ban-system
  - networking-chat-system
  - networking-lag-compensation
  - networking-message-ordering
  - networking-performance-monitoring
  - networking-player-spawning
  - networking-prediction-reconciliation
  - networking-trading-system
  - physics-chain-dynamics
  - ai-squad-tactics
  - ai-threat-assessment
  - audio-ducking-sidechains
  - cinemachine-aim-assist
  - networking-account-recovery
  - networking-bandwidth-optimization
  - networking-battle-pass
  - networking-client-authority
  - networking-connection-management
  - networking-friend-system
  - networking-leaderboard
  - networking-matchmaking
  - networking-player-persistence
  - networking-pvp-ranking
  - networking-rpc-system
  - networking-spectator-mode
  - networking-statistics-synchronization
  - physics-hair-dynamics
  - physics-joint-constraints
  - terrain-blending-shaders
  - terrain-cave-systems
  - terrain-heightmap-import
  - terrain-noise-functions
  - terrain-normal-generation
  - terrain-path-carving
  - terrain-shape-tools
  - terrain-streaming
  - terrain-water-integration
  - audio-dialogue-system
  - ai-behavior-switching
  - ai-communication-network
  - ai-crowd-simulation
  - ai-environmental-awareness
  - ai-formation-control
  - automated-testing-framework
  - cinemachine-virtual-camera
  - compatibility-testing
  - csharp-async-await
  - debug-renderer-debugging
  - debug-script-debugging
  - debug-shader-debugging
  - material-mipmap-chains
  - material-visual-debugging
  - networking-antiCheat-detection
  - networking-auction-system
  - networking-cross-progression
  - networking-interpolation
  - networking-packet-loss-handling
  - networking-presence-system
  - networking-region-selection
  - networking-rollback-resimulation
  - networking-server-load-balancing
  - networking-server-replication
  - networking-state-synchronization
  - physics-constraint-optimization
  - physics-terrain-deformation
  - terrain-advanced-editing
  - terrain-biome-definition
  - terrain-brush-settings
  - terrain-cliff-generation
  - terrain-detail-meshes
  - terrain-dynamic-modification
  - terrain-erosion-simulation
  - terrain-grass-placement
  - terrain-heightfield-editing
  - terrain-layer-management
  - terrain-lightmap-generation
  - terrain-lod-optimization
  - terrain-memory-management
  - terrain-multi-layer-textures
  - terrain-neighbor-blending
  - terrain-performance-tuning
  - terrain-physics-colliders
  - terrain-procedural-generation
  - terrain-shadow-caching
  - terrain-sound-surfaces
  optional:
  - terrain-splat-mapping
  - terrain-texture-painting
  - terrain-transition-zones
  - terrain-tree-painting
  - terrain-vegetation-placement
validation_gates:
- yaml-frontmatter-validation
- skill-naming-convention
- description-quality
- token-efficiency
- risk-level-appropriateness
- cross-skill-consistency
- response-patterns-actionability
- mandates-clarity
primary_agent: tech-lead
secondary_agents:
- production-lead
complexity_score: 5.0
skill_density: 176.0
estimated_skills_needed: 176
integration_level: critical
phase: '3'
phase3_integration_date: '2026-03-21'
---


# GDPR Compliance & Data Privacy Setup

This workflow ensures your game complies with GDPR (EU), CCPA (California), and other privacy regulations for user data collection and storage.

## Prerequisites

- Legal review recommended
- Privacy policy template (IAPP, DLA Piper templates available)
- Data storage infrastructure (cloud database with encryption)
- User consent management system
- 1-2 weeks for full implementation

## Context

Privacy regulations impose strict requirements on data collection, storage, user rights (access, deletion), and consent management. Non-compliance risks substantial fines (up to 4% revenue or €20M for GDPR).

// turbo-all

## Phase 1: Understand Regulatory Requirements

| Regulation | Scope | Key Requirement |
|---|---|---|
| **GDPR** | EU/UK players | Explicit opt-in consent, right to deletion |
| **CCPA** | California players | Right to know, right to delete, opt-out |
| **LGPD** | Brazil players | Legitimate purpose required, data portability |
| **PIPL** | China players | Data localization, government cooperation |

## Phase 2: Data Inventory & Audit

1. **Map All Collected Data:**
   ```plaintext
   What data do you collect?
   - Player name / username
   - Device ID / IDFA
   - IP address
   - Age/DoB
   - Location (GPS coordinates)
   - Game progress / gameplay data
   - Payment information
   - Device specifications
   - Advertising ID
   - Analytics events
   - Crash reports
   - Chat messages
   ```

2. **Document Collection Purpose:**
   ```plaintext
   For each data point, answer:
   - WHY do you collect it? (legitimate interest, consent, contract)
   - WHERE is it stored? (on-device, cloud database specify location)
   - HOW LONG do you keep it? (retention policy)
   - WHO has access? (internal team, third-party services)
   - CAN it be shared? (with advertisers, analytics partners)
   ```

## Phase 3: Create Privacy Policy & Consent Dialog

1. **Draft Privacy Policy:**
   ```markdown
   Required sections:
   - What information we collect
   - How we use it
   - Data retention periods
   - Your rights (access, deletion, portability)
   - Contact information for privacy officer
   - For minors: Parental consent requirements (COPPA)
   ```

2. **Implement Consent Dialog (On First Launch):**
   ```csharp
   public class ConsentDialogManager : MonoBehaviour
   {
       public void ShowConsentDialog()
       {
           // Display dialog with:
           // - Description of data collection
           // - "Agree" and "Disagree" buttons
           // - Link to full privacy policy
           // - Age gate (if game is for children)

           if (PlayerPrefs.GetInt("ConsentShown", 0) == 0)
           {
               // Show dialog
               ShowDialog("We collect gameplay data to improve...",
                  () => SetConsent(true),
                  () => SetConsent(false));

               PlayerPrefs.SetInt("ConsentShown", 1);
           }
       }

       private void SetConsent(bool consented)
       {
           PlayerPrefs.SetInt("AnalyticsConsent", consented ? 1 : 0);
           PlayerPrefs.SetString("ConsentDate", System.DateTime.Now.ToString());
           // Disable analytics if not consented
       }
   }
   ```

3. **Age Verification (For COPPA Compliance):**
   ```csharp
   public class AgeGate : MonoBehaviour
   {
       private const int CHILD_AGE_THRESHOLD = 13;

       public void VerifyAge(int birthYear)
       {
           int age = System.DateTime.Now.Year - birthYear;

           if (age < CHILD_AGE_THRESHOLD)
           {
               // COPPA: Under 13 requires parental consent
               PlayerPrefs.SetInt("RequiresParentalConsent", 1);
               ShowParentalConsentForm();
           }
           else
           {
               // Can proceed with normal consent
               ShowStandardConsentForm();
           }
       }
   }
   ```

## Phase 4: Implement User Data Rights

1. **Right to Access (Data Download):**
   ```csharp
   public class DataExportManager
   {
       public void ExportPlayerData(string playerID)
       {
           var playerData = new {
               ID = playerID,
               CreatedAt = GetPlayerCreationDate(playerID),
               GameProgress = GetGameProgress(playerID),
               AnalyticsEvents = GetAnalyticsHistory(playerID),
               PurchaseHistory = GetPurchaseHistory(playerID)
           };

           string jsonData = JsonUtility.ToJson(playerData, true);
           System.IO.File.WriteAllText($"PlayerData_{playerID}.json", jsonData);

           // Encrypt before sending
           SendDataToPlayerEmail(playerID, jsonData);
       }
   }
   ```

2. **Right to Deletion (GDPR "Right to be Forgotten"):**
   ```csharp
   public class AccountDeletionManager
   {
       public void RequestAccountDeletion(string playerID)
       {
           // Log deletion request with timestamp
           LogDeletionRequest(playerID);

           // Start 30-day grace period
           DateTime deletionDate = System.DateTime.Now.AddDays(30);
           PlayerPrefs.SetString($"DeletionRequest_{playerID}", deletionDate.ToString());

           // Delete from analytics immediately
           RemoveFromAnalytics(playerID);

           // Mark for deletion (don't delete immediately - compliance requires audit trail)
           MarkAccountForDeletion(playerID, deletionDate);
       }

       public void ConfirmDeletion(string playerID)
       {
           // After grace period, permanently delete:
           DeleteFromDatabase(playerID);
           DeleteFromBackups(playerID);
           AuditLog($"Account {playerID} permanently deleted");
       }
   }
   ```

3. **Right to Portability (Export in Standard Format):**
   ```csharp
   public void ExportGameProgressPortable(string playerID)
   {
       // Export in standard format (JSON)
       var exportData = new {
           Username = GetPlayerName(playerID),
           Level = GetPlayerLevel(playerID),
           Achievements = GetPlayerAchievements(playerID),
           Inventory = GetPlayerInventory(playerID),
           Statistics = GetPlayerStatistics(playerID)
       };

       string json = JsonUtility.ToJson(exportData, true);
       // Allow player to download or import to another game
   }
   ```

## Phase 5: Secure Data Storage & Encryption

1. **Encrypt Sensitive Game Data:**
   ```csharp
   using System.Security.Cryptography;
   using System.Text;

   public class DataEncryption
   {
       public static string EncryptData(string plaintext, string key)
       {
           using (Aes aes = Aes.Create())
           {
               aes.Key = Encoding.UTF8.GetBytes(key);
               ICryptoTransform encryptor = aes.CreateEncryptor(aes.Key, aes.IV);

               using (MemoryStream ms = new MemoryStream())
               {
                   ms.Write(aes.IV, 0, aes.IV.Length);
                   using (CryptoStream cs = new CryptoStream(ms, encryptor, CryptoStreamMode.Write))
                   {
                       using (StreamWriter sw = new StreamWriter(cs))
                       {
                           sw.Write(plaintext);
                       }
                   }
                   return Convert.ToBase64String(ms.ToArray());
               }
           }
       }
   }
   ```

2. **Local Data Storage (On-Device):**
   ```csharp
   #if UNITY_IOS
   // iOS: Use Keychain
   SecurePlayerPrefs.SetString("api_token", encryptedToken);
   #elif UNITY_ANDROID
   // Android: Use EncryptedSharedPreferences
   EncryptedSharedPreferences.getInstance().edit().putString("api_token", encryptedToken).apply();
   #endif
   ```

## Phase 6: Third-Party Compliance

1. **Audit All Third-Party SDKs:**
   ```markdown
   For each SDK/service used:
   - Does it process player data?
   - Where is data stored geographically?
   - Do they have GDPR/CCPA certifications?
   - Is a Data Processing Agreement (DPA) required?

   Examples to check:
   - Analytics: Firebase, Amplitude, Mixpanel
   - Ads: AdMob, Unity Ads, Facebook Audience Network
   - Payments: Stripe, Braintree
   - Social: Facebook SDK, Discord SDK
   ```

2. **Disable Tracking for Non-Consented Users:**
   ```csharp
   if (PlayerPrefs.GetInt("AnalyticsConsent", 0) == 1)
   {
       EnableAnalytics();
   }
   else
   {
       // Don't send data to Firebase, Mixpanel, etc.
       DisableThirdPartyTracking();
   }
   ```

## Phase 7: Documentation & Record Keeping

1. **Maintain Data Processing Records:**
   ```plaintext
   Document for compliance audits:
   - Data inventory (what you collect)
   - Consent records (who approved, when)
   - Deletion requests (log with dates)
   - DPA agreements with vendors
   - Privacy impact assessments (for high-risk features)
   - Incident response plan (for breaches)
   ```

2. **Document Consent Acceptance:**
   ```csharp
   public void LogConsentAcceptance()
   {
       var consentRecord = new {
           PlayerID = GetPlayerID(),
           Timestamp = System.DateTime.UtcNow,
           ConsentVersion = "v1.0",
           PrivacyPolicyURL = "https://game.com/privacy",
           IsConsented = true
       };

       SaveToAuditLog(JsonUtility.ToJson(consentRecord));
   }
   ```

## Phase 8: Incident Response & Breach Notification

1. **Data Breach Response Plan:**
   ```markdown
   If a breach occurs:
   1. Notify players within 72 hours (GDPR requirement)
   2. Report to relevant data protection authority
   3. Document breach details and remediation steps
   4. Preserve evidence for investigation
   5. Offer identity theft protection if necessary
   ```

2. **Breach Notification Template:**
   ```
   Subject: Important Security Notice

   We discovered an unauthorized access to [AFFECTED DATA].
   The breach affected [NUMBER] players.
   We have [REMEDIATION STEP].
   Your rights: [RIGHTS INFORMATION]
   Contact us: privacy@company.com
   ```

## Verification Checklist

- [ ] Privacy policy drafted and reviewed by legal
- [ ] Consent dialog collecting explicit user agreement
- [ ] Age gate implemented (if game for all ages)
- [ ] Data inventory documented
- [ ] Encryption implemented for sensitive data
- [ ] User data export feature working
- [ ] User deletion feature working (with audit trail)
- [ ] Third-party SDKs compliance verified
- [ ] Opt-out mechanism for all tracking
- [ ] Parental consent form (for COPPA- COPPA compliance if needed)
- [ ] Audit logging for all data access
- [ ] Breach notification plan documented

## Common Issues & Fixes

| Issue | Solution |
|-------|----------|
| "We don't know what data we collect" | Audit all SDKs, check Backend API logs, review PlayerPrefs data |
| GDPR fine received | Consult data privacy lawyer, implement corrective measures immediately |
| User deletion incomplete | Ensure deletion covers database, cloud storage, and analytics backends |
| Third-party still tracking after opt-out | Contact vendor, request account deletion, disable SDK initialization |

## Related Topics

- See `/analytics-integration` for consent flow
- Refer to `@security-specialist` skill for encryption details
- Check `/project-health-check` for compliance monitoring