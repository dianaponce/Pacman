import sys

# script to run debug mode
scriptPath = '/Users/dianaponce/Git_projects/Pacman/Reinforcement/pacman.py'
sys.argv = [scriptPath,'-p','PacmanQAgent','-n','2','-a','numTraining=2']
execfile(scriptPath)

#python pacman.py -p PacmanQAgent -n 10 -l smallGrid -a numTraining=10