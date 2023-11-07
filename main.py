from login import driver, logging_in
import fast_action
import gym
import ring

driver.get("https://g2.gangsters.pl/")
driver.maximize_window()

logging_in()
fast_action.fast_action()
fast_action.fast_action_make(30, 4, 4, 7)
# gym.gym()
# gym.atlas(2,'100')
# gym.treadmill(2,'100')
# gym.rower(2,'100')
# gym.bench(50,'100')
# gym.atlas_max(50,'100')
# ring.ring()
# ring.ring_fight(5)