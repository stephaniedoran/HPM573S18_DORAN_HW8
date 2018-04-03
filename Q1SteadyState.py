# Present to the casino’s owner the change and the percentage change
# in their reward if they use an unfair coin for which the probability
# of head is 45%.

import Classes as Cls

# create a cohort of patients for when the drug is not available
cohortFair = Cls.SetOfGames(
    id=1,
    prob_head=0.5,
    n_games=1000
    )
# simulate the cohort
FairOutcome = cohortFair.simulation()

# create a cohort of patients for when the drug is available
cohortUnfair = Cls.SetOfGames(
    id=2,
    prob_head=0.45,
    n_games=1000)

# simulate the cohort
UnfairOutcome = cohortUnfair.simulation()

# print outcomes of each cohort
print('For the casino owner')
print('When the coin is fair, the average reward is:', FairOutcome.get_ave_reward(), 'with a 95% confidence interval:',
      FairOutcome.get_CI_reward(0.05))
print('When the coin is unfair, the average reward is:', UnfairOutcome.get_ave_reward(),
      'with a 95% confidence interval:', UnfairOutcome.get_CI_reward(0.05))
print('The change in average reward is', (UnfairOutcome.get_ave_reward() - FairOutcome.get_ave_reward()))
