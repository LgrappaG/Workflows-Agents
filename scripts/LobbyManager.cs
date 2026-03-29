using UnityEngine;
using Unity.Netcode;
using UnityEngine.UI;

namespace Antigravity.Multiplayer
{
    /// <summary>
    /// Simplified lobby manager to handle hosting and joining sessions via MCP-generated UI.
    /// </summary>
    public class LobbyManager : MonoBehaviour
    {
        public Button hostButton;
        public Button clientButton;
        public InputField addressInput;

        private void Start()
        {
            if (hostButton != null) hostButton.onClick.AddListener(StartHost);
            if (clientButton != null) clientButton.onClick.AddListener(StartClient);
        }

        public void StartHost()
        {
            NetworkManager.Singleton.StartHost();
            Debug.Log("[LobbyManager] Started as HOST.");
        }

        public void StartClient()
        {
            // In a real transport setup, we would set the IP from addressInput
            NetworkManager.Singleton.StartClient();
            Debug.Log("[LobbyManager] Started as CLIENT connecting to: " + (addressInput?.text ?? "localhost"));
        }

        public void Shutdown()
        {
            NetworkManager.Singleton.Shutdown();
            Debug.Log("[LobbyManager] Networking shutdown.");
        }
    }
}
