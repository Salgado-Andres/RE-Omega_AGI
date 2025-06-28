import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import asyncio

from src.agents import E1Agent, E2Agent, E3Agent, E4Agent, E5Agent, E6Agent, E7LogOS


async def run_all():
    agents = [E1Agent(), E2Agent(), E3Agent(), E4Agent(), E5Agent(), E6Agent(), E7LogOS()]
    data = "test"
    for agent in agents:
        if hasattr(agent, 'compile'):
            await agent.compile(data)
        elif hasattr(agent, 'map'):
            await agent.map(data)
        elif hasattr(agent, 'critique'):
            await agent.critique(data)
        elif hasattr(agent, 'analyze'):
            await agent.analyze(data)
        elif hasattr(agent, 'simulate'):
            await agent.simulate(data)
        elif hasattr(agent, 'forecast'):
            await agent.forecast(data)
        elif hasattr(agent, 'awaken'):
            await agent.awaken(data)


def test_agents_run():
    asyncio.run(run_all())
