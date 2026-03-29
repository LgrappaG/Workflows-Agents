using UnityEngine;
using Unity.Netcode;
using Antigravity.Logic;

namespace Antigravity.Multiplayer
{
    /// <summary>
    /// Synchronizes survival stats across the network using NetworkVariables.
    /// This extends the base survival logic for multiplayer compatibility.
    /// </summary>
    public class NetworkSurvivalHandler : NetworkBehaviour
    {
        private SurvivalHandler _localHandler;

        // Note: In a real implementation, we would use a NetworkList or separate NetworkVariables 
        // per stat. This is a simplified synchronization bridge.
        public NetworkVariable<float> syncHunger = new NetworkVariable<float>(100f, NetworkVariableReadPermission.Everyone, NetworkVariableWritePermission.Server);
        public NetworkVariable<float> syncThirst = new NetworkVariable<float>(100f, NetworkVariableReadPermission.Everyone, NetworkVariableWritePermission.Server);

        public override void OnNetworkSpawn()
        {
            _localHandler = GetComponent<SurvivalHandler>();
            
            if (IsServer)
            {
                // Link local values to network variables
                InvokeRepeating(nameof(UpdateNetworkVariables), 0.1f, 0.1f);
            }
            
            if (IsClient && !IsOwner)
            {
                // Disable local simulation for non-owners (let the server/owner handle it)
                if (_localHandler != null) _localHandler.enabled = false;
            }
        }

        private void UpdateNetworkVariables()
        {
            if (_localHandler == null) return;

            if (_localHandler.currentValues.TryGetValue("Hunger", out float hunger))
                syncHunger.Value = hunger;
            
            if (_localHandler.currentValues.TryGetValue("Thirst", out float thirst))
                syncThirst.Value = thirst;
        }

        private void Update()
        {
            if (IsClient && !IsOwner && _localHandler != null)
            {
                // Update local dictionary for UI consistency on remotes
                if (_localHandler.currentValues.ContainsKey("Hunger"))
                    _localHandler.currentValues["Hunger"] = syncHunger.Value;
                
                if (_localHandler.currentValues.ContainsKey("Thirst"))
                    _localHandler.currentValues["Thirst"] = syncThirst.Value;
            }
        }
    }
}
