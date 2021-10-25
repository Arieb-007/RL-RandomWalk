import numpy as np
import gym

class SRWE(gym.Env) :
  
  def __init__(self):
    self.state_space = np.arange(9) 
    self.action_space = np.arange(2) 
    self.state = len(self.state_space)//2
    self.terminal = [0,8]
    self.reward_space = [0,1]
    self.prev_state = None

  def reset(self):
    self.state = len(self.state_space)//2
    self.prev_state=None
    return self.state,0

  def seed(self,seed):
    np.random.random(seed)

  def step(self,action):
    self.prev_state = self.state
    reward = 0
    done = 0
    p = np.random.random()
    if(action==0):
      if(p<0.16) : self.state += 1
      elif(p>0.5) : self.state -=1

    if(action==1):
      if(p<0.16) : self.state -= 1
      elif(p>0.5) : self.state +=1

    if(self.state==8) : 
      reward = 1
      done = 1
    
    if(self.state==0): done = 1

    return self.state,reward,done
