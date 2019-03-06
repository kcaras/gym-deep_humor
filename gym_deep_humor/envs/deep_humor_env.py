import gym
from gym import error, spaces, utils
from gym.utils import seeding
import DeepQA.chatbot.chatbot as chatbot
import tensorflow as tf
class DeepHumorEnv(gym.Env):
  metadata = {'render.modes': ['human']}

  def __init__(self):
    with tf.Session() as sess:
      self.chat = chatbot.get_chatbot(sess, args)
  def step(self, action):
    pass
  def reset(self):
    pass
  def render(self, mode='human'):
    pass
  def close(self):
    pass