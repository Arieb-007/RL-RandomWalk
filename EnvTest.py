env = SRWE()
count = np.zeros([len(env.state_space)])
print("[state ,action, same state prob ,   state-1 prob ,  state+1 prob ]")
for s in range(1,8) :
  
  for a in env.action_space  :
    count = np.zeros([len(env.state_space)])
    for e in range(100000):
      s_n,r,done = env.step(a)
      count[s_n]+=1
      env.state = s
    if(a==0): action = 'LEFT'
    else : action = 'RIGHT'
    l = [s, action,count[s]/e,count[s-1]/e,count[s+1]/e]
    
    print(l)
