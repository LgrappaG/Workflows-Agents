using UnityEngine;
using Unity.Netcode;

namespace Antigravity.Multiplayer
{
    /// <summary>
    /// Handles RPC calls to synchronize deterministic actions (like Parkour) across all clients.
    /// </summary>
    public class ActionSyncer : NetworkBehaviour
    {
        /// <summary>
        /// Triggered by the owner to notify everyone that a parkour action started.
        /// </summary>
        [ServerRpc]
        public void RequestActionSyncServerRpc(string actionName, Vector3 impactPoint)
        {
            // The server broadcasts this to all clients
            NotifyActionClientRpc(actionName, impactPoint);
        }

        [ClientRpc]
        private void NotifyActionClientRpc(string actionName, Vector3 impactPoint)
        {
            if (IsOwner) return; // Owner already played local visual/audio

            Debug.Log($"[ActionSyncer] Remote action detected: {actionName} at {impactPoint}");
            // Trigger visual representation on remote proxy
            // Example: GetComponent<Animator>().Play(actionName);
        }
    }
}
