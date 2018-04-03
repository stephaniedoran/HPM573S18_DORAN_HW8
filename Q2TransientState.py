# Present to the casino’s owner the change and the percentage change
# in their reward if they use an unfair coin for which the probability
# of head is 45%.

import Classes as Cls

cohortFair = Cls.MultipleGameSets(
    ids=range(1000),
    prob_head=0.5,
    n_games_in_a_set=10
    )
# simulate the cohort
cohortFair.simulation()

# create a cohort of patients for when the drug is available
cohortUnfair = Cls.MultipleGameSets(
    ids=range(1000),
    prob_head=0.45,
    n_games_in_a_set=10)

# simulate the cohort
cohortUnfair.simulation()

# print outcomes of each cohort
print('For the gambler,')
print('When the coin is fair, the average reward is:', cohortFair.get_mean_total_reward(),
      'the 95% projection interval is:', cohortFair.get_PI_total_reward(0.05))
print('When the coin is unfair, the average reward is:', cohortUnfair.get_mean_total_reward(),
      'the 95% projection interval is:', cohortUnfair.get_PI_total_reward(0.05))
print('The change in average reward is', (cohortUnfair.get_mean_total_reward() - cohortFair.get_mean_total_reward()))
