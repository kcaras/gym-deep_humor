from gym.envs.registration import register

register(
    id='deep_humor-v0',
    entry_point='gym_deep_humor.envs:FooEnv',
)
register(
    id='deep_humor-extrahard-v0',
    entry_point='gym_deep_humor.envs:FooExtraHardEnv',
)