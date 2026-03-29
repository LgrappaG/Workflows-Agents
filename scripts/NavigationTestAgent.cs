using UnityEngine;
using UnityEngine.AI;

namespace Antigravity.Bonus
{
    /// <summary>
    /// An automated agent that tests if points in the world are reachable via NavMesh.
    /// Used by MCP to verify level design and parkour pathing.
    /// </summary>
    [RequireComponent(typeof(NavMeshAgent))]
    public class NavigationTestAgent : MonoBehaviour
    {
        private NavMeshAgent _agent;
        public bool isTesting = false;
        public Vector3 currentTarget;

        public delegate void OnTestResult(bool success);
        public OnTestResult testCallback;

        private void Awake()
        {
            _agent = GetComponent<NavMeshAgent>();
            _agent.speed = 10f; // Fast for testing
        }

        /// <summary>
        /// Commands the agent to test a path to a specific target.
        /// </summary>
        public void TestPathTo(Vector3 target, OnTestResult callback = null)
        {
            currentTarget = target;
            testCallback = callback;
            isTesting = true;
            _agent.SetDestination(target);
        }

        private void Update()
        {
            if (!isTesting) return;

            if (!_agent.pathPending)
            {
                if (_agent.remainingDistance <= _agent.stoppingDistance)
                {
                    if (!_agent.hasPath || _agent.velocity.sqrMagnitude == 0f)
                    {
                        FinishTest(true);
                    }
                }
                else if (_agent.pathStatus == NavMeshPathStatus.PathPartial || _agent.pathStatus == NavMeshPathStatus.PathInvalid)
                {
                    FinishTest(false);
                }
            }
        }

        private void FinishTest(bool success)
        {
            isTesting = false;
            Debug.Log($"[NavigationTest] Path to {currentTarget} Result: {(success ? "SUCCESS" : "FAILED")}");
            testCallback?.Invoke(success);
        }
    }
}
