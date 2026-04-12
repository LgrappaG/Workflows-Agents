"""
Intelligence Router
===================

Multi-agent decision making with consensus voting.

Responsibilities:
- Coordinate decisions across multiple agents
- Consensus voting on critical decisions
- Agent conflict resolution
- Escalation hierarchy management
- Decision audit trails
"""

from datetime import datetime
from typing import Dict, List, Any, Optional, Callable
from collections import defaultdict
from enum import Enum


class VotingStrategy(Enum):
    """Voting strategies for consensus"""
    MAJORITY = "majority"  # >50%
    SUPERMAJORITY = "supermajority"  # >66%
    UNANIMOUS = "unanimous"  # 100%
    ANY_AFFIRMATIVE = "any_affirmative"  # At least one yes


class Vote:
    """Represents a single vote from an agent"""

    def __init__(self, agent_name: str, decision: str, confidence: float = 1.0, rationale: str = ""):
        self.agent_name = agent_name
        self.decision = decision  # "approve", "reject", "abstain"
        self.confidence = confidence  # 0.0 - 1.0
        self.rationale = rationale
        self.timestamp = datetime.now()

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        return {
            "agent": self.agent_name,
            "decision": self.decision,
            "confidence": f"{self.confidence:.2f}",
            "rationale": self.rationale,
            "timestamp": self.timestamp.isoformat()
        }


class VotingRound:
    """Represents a voting round for a decision"""

    def __init__(self, decision_id: str, decision_context: str, voting_strategy: VotingStrategy = VotingStrategy.MAJORITY):
        self.decision_id = decision_id
        self.decision_context = decision_context
        self.voting_strategy = voting_strategy
        self.votes = []
        self.final_decision = None
        self.created_at = datetime.now()
        self.closed_at = None

    def add_vote(self, vote: Vote):
        """Add a vote"""
        self.votes.append(vote)

    def close_voting(self) -> Dict[str, Any]:
        """
        Close voting and calculate result.
        """
        self.closed_at = datetime.now()

        if not self.votes:
            return {
                "decision_id": self.decision_id,
                "result": "no_votes",
                "final_decision": None
            }

        # Count votes
        vote_counts = defaultdict(int)
        total_affirmative_confidence = 0

        for vote in self.votes:
            if vote.decision != "abstain":
                vote_counts[vote.decision] += 1

            if vote.decision == "approve":
                total_affirmative_confidence += vote.confidence

        total_votes = len([v for v in self.votes if v.decision != "abstain"])

        # Apply voting strategy
        result = self._apply_voting_strategy(vote_counts, total_votes)

        return {
            "decision_id": self.decision_id,
            "decision_context": self.decision_context,
            "voting_strategy": self.voting_strategy.value,
            "total_votes": total_votes,
            "vote_breakdown": dict(vote_counts),
            "result": result,
            "final_decision": result,
            "votes": [v.to_dict() for v in self.votes],
            "average_confidence": total_affirmative_confidence / len([v for v in self.votes if v.decision == "approve"]) if any(v.decision == "approve" for v in self.votes) else 0
        }

    def _apply_voting_strategy(self, vote_counts: Dict[str, int], total_votes: int) -> str:
        """Apply voting strategy to determine result"""
        if self.voting_strategy == VotingStrategy.MAJORITY:
            approve_count = vote_counts.get("approve", 0)
            if approve_count > total_votes / 2:
                return "approved"
            else:
                return "rejected"

        elif self.voting_strategy == VotingStrategy.SUPERMAJORITY:
            approve_count = vote_counts.get("approve", 0)
            if approve_count > total_votes * 2 / 3:
                return "approved"
            else:
                return "rejected"

        elif self.voting_strategy == VotingStrategy.UNANIMOUS:
            approve_count = vote_counts.get("approve", 0)
            if approve_count == total_votes:
                return "approved"
            else:
                return "rejected"

        elif self.voting_strategy == VotingStrategy.ANY_AFFIRMATIVE:
            if vote_counts.get("approve", 0) > 0:
                return "approved"
            else:
                return "rejected"

        return "unknown"

    def is_open(self) -> bool:
        """Check if voting is still open"""
        return self.closed_at is None


class AgentConsensus:
    """Manages consensus building across agents"""

    def __init__(self, required_agents: List[str] = None):
        self.required_agents = required_agents or []
        self.voting_rounds = {}  # decision_id -> VotingRound
        self.decision_history = []

    def create_voting_round(
        self,
        decision_id: str,
        decision_context: str,
        voting_strategy: VotingStrategy = VotingStrategy.MAJORITY
    ) -> VotingRound:
        """Create a new voting round"""
        round = VotingRound(decision_id, decision_context, voting_strategy)
        self.voting_rounds[decision_id] = round
        return round

    def submit_vote(self, decision_id: str, vote: Vote):
        """Submit a vote to a voting round"""
        if decision_id not in self.voting_rounds:
            raise ValueError(f"Voting round {decision_id} not found")

        round = self.voting_rounds[decision_id]
        if not round.is_open():
            raise ValueError(f"Voting round {decision_id} is closed")

        round.add_vote(vote)

    def finalize_decision(self, decision_id: str) -> Dict[str, Any]:
        """Finalize a decision by closing the voting round"""
        if decision_id not in self.voting_rounds:
            raise ValueError(f"Voting round {decision_id} not found")

        round = self.voting_rounds[decision_id]
        result = round.close_voting()

        # Store in history
        self.decision_history.append(result)

        return result

    def get_consensus_status(self, decision_id: str) -> Dict[str, Any]:
        """Get current status of a voting round"""
        if decision_id not in self.voting_rounds:
            return {}

        round = self.voting_rounds[decision_id]
        votes = [v.to_dict() for v in round.votes]

        return {
            "decision_id": decision_id,
            "decision_context": round.decision_context,
            "is_open": round.is_open(),
            "votes_received": len(round.votes),
            "required_agents": len(self.required_agents),
            "votes": votes
        }


class ConflictResolver:
    """Resolves conflicts between agents"""

    @staticmethod
    def resolve_priority_conflict(agent_decisions: Dict[str, str]) -> str:
        """
        Resolve conflict using agent priority.
        Agent priority (descending): deploy > sync > validation > knowledge
        """
        priority = {"deploy": 4, "sync": 3, "validation": 2, "knowledge": 1}

        best_agent = max(agent_decisions.keys(), key=lambda x: priority.get(x, 0))
        return agent_decisions[best_agent]

    @staticmethod
    def resolve_confidence_conflict(agent_decisions: Dict[str, tuple]) -> str:
        """
        Resolve conflict using decision confidence.
        agent_decisions: {agent_name: (decision, confidence)}
        """
        best_agent = max(agent_decisions.keys(), key=lambda x: agent_decisions[x][1])
        return agent_decisions[best_agent][0]

    @staticmethod
    def resolve_voting_conflict(agent_decisions: Dict[str, str]) -> str:
        """Resolve conflict using majority voting"""
        from collections import Counter
        decisions = list(agent_decisions.values())
        most_common = Counter(decisions).most_common(1)
        return most_common[0][0] if most_common else "undecided"


class DecisionAuditTrail:
    """Tracks all decisions and reasoning"""

    def __init__(self):
        self.decisions = []

    def record_decision(
        self,
        decision_id: str,
        decision_context: str,
        decision: str,
        agents_involved: List[str],
        reasoning: str,
        conflict_resolution_strategy: Optional[str] = None
    ):
        """Record a decision with full audit trail"""
        entry = {
            "timestamp": datetime.now().isoformat(),
            "decision_id": decision_id,
            "decision_context": decision_context,
            "final_decision": decision,
            "agents": agents_involved,
            "reasoning": reasoning,
            "conflict_resolution": conflict_resolution_strategy
        }

        self.decisions.append(entry)

    def get_audit_trail(self, decision_id: Optional[str] = None) -> List[Dict[str, Any]]:
        """Get audit trail for a decision or all decisions"""
        if decision_id:
            return [d for d in self.decisions if d["decision_id"] == decision_id]
        return self.decisions

    def get_agent_contribution(self, agent_name: str) -> Dict[str, Any]:
        """Get statistics on agent contributions"""
        agent_decisions = [d for d in self.decisions if agent_name in d.get("agents", [])]

        return {
            "agent": agent_name,
            "total_decisions": len(agent_decisions),
            "decisions": agent_decisions
        }


class IntelligenceRouter:
    """Main intelligence router for multi-agent coordination"""

    def __init__(self, agents: List[str] = None):
        self.agents = agents or ["deploy", "sync", "validation", "knowledge"]
        self.consensus = AgentConsensus(self.agents)
        self.conflict_resolver = ConflictResolver()
        self.audit_trail = DecisionAuditTrail()
        self.routing_decisions = []

    def route_decision(
        self,
        decision_context: Dict[str, Any],
        agent_recommendations: Dict[str, Dict[str, Any]],
        voting_strategy: VotingStrategy = VotingStrategy.MAJORITY
    ) -> Dict[str, Any]:
        """
        Route a decision through multi-agent consensus voting.

        Args:
            decision_context: {"goal": "...", "environment": "...", "priority": "..."}
            agent_recommendations: {agent_name: {"decision": "...", "confidence": 0.8, "rationale": "..."}}
            voting_strategy: Strategy for consensus

        Returns:
            Final routing decision with full audit trail
        """
        decision_id = f"route_{datetime.now().timestamp()}"

        # Create voting round
        voting_round = self.consensus.create_voting_round(
            decision_id,
            decision_context.get("goal", "unknown"),
            voting_strategy
        )

        # Collect votes from all agents
        for agent_name, recommendation in agent_recommendations.items():
            vote = Vote(
                agent_name=agent_name,
                decision=recommendation.get("decision", "abstain"),
                confidence=recommendation.get("confidence", 0.5),
                rationale=recommendation.get("rationale", "")
            )
            self.consensus.submit_vote(decision_id, vote)

        # Finalize voting
        voting_result = self.consensus.finalize_decision(decision_id)

        # Resolve any conflicts if needed
        if voting_result["result"] in ["multiple", "split"]:
            final_decision = self._resolve_voting_conflict(agent_recommendations)
            conflict_strategy = "voting"
        else:
            final_decision = voting_result["result"]
            conflict_strategy = None

        # Record audit trail
        self.audit_trail.record_decision(
            decision_id=decision_id,
            decision_context=str(decision_context),
            decision=final_decision,
            agents_involved=list(agent_recommendations.keys()),
            reasoning=f"Multi-agent consensus: {voting_result}",
            conflict_resolution_strategy=conflict_strategy
        )

        routing_result = {
            "decision_id": decision_id,
            "decision_context": decision_context,
            "final_decision": final_decision,
            "voting_round": voting_result,
            "audit_trail": self.audit_trail.get_audit_trail(decision_id)[-1]
        }

        self.routing_decisions.append(routing_result)

        return routing_result

    def _resolve_voting_conflict(self, recommendations: Dict[str, Dict[str, Any]]) -> str:
        """Resolve voting conflicts"""
        agent_decisions = {
            agent: (rec["decision"], rec.get("confidence", 0.5))
            for agent, rec in recommendations.items()
        }

        # Use confidence-based resolution
        return self.conflict_resolver.resolve_confidence_conflict(agent_decisions)

    def escalate_to_leadership(self, decision_context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Escalate decision to leadership level.
        Leadership agents: deploy > sync > validation > knowledge
        """
        return {
            "escalated": True,
            "decision_context": decision_context,
            "leadership_agents": ["deploy", "sync"],
            "escalation_reason": "Consensus not reached at specialist level",
            "timestamp": datetime.now().isoformat()
        }

    def get_routing_statistics(self) -> Dict[str, Any]:
        """Get statistics on routing decisions"""
        return {
            "total_decisions": len(self.routing_decisions),
            "agents": self.agents,
            "audit_trail_entries": len(self.audit_trail.decisions),
            "agent_contributions": {
                agent: self.audit_trail.get_agent_contribution(agent)
                for agent in self.agents
            }
        }

    def get_agent_performance(self, agent_name: str) -> Dict[str, Any]:
        """Get performance metrics for an agent"""
        contribution = self.audit_trail.get_agent_contribution(agent_name)

        return {
            "agent": agent_name,
            "decisions_contributed": contribution["total_decisions"],
            "decision_history": contribution["decisions"]
        }
