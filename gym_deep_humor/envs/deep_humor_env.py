import gym
from gym import error, spaces, utils
from gym.utils import seeding
import tensorflow as tf
import argparse
class DeepHumorEnv(gym.Env):
  metadata = {'render.modes': ['human']}

  def __init__(self):
    pass

  def step(self, action):
    pass

  def reset(self):
    pass
  def render(self, mode='human'):
    pass
  def close(self):
    pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Train a reinforcement learner.')

    parser.add_argument('-f', '--model-file', required=True, help='The name of the model to load and save.')
    parser.add_argument('-t', '--rl-test', help='Test the current model.', action='store_true')
    parser.add_argument('-d', '--debug-print', help="Display more detail about the chatbot's decisions.", action='store_true')
    parser.add_argument('-i', '--interactive', help='Directly talk to the chatbot instead of watching it talk to another chatbot.', action='store_true')
    parser.add_argument('-o', '--show-other', help="Whether to show the unchosen chatbot's would-be response.", action='store_true')
    parser.add_argument('-s', '--reduce-swear', help="Whether to reduce the amount of swearing used by the humor chatbot.", action='store_true')
    args, _ = parser.parse_known_args()
