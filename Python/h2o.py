import threading 
from threading import Semaphore
from typing import List

class H2O:
	def __init__(self):
		self.oxy = 0
		self.hyd = 0
		self.ox_sem = Semaphore(1) 
		self.hy_sem = Semaphore(2)
		

	def relOxy(self):
		print("O")

	def relHy(self):
		print("H")

	def reset(self):
		if self.oxy == 1 and self.hyd == 2:
			self.oxy = 0
			self.hyd = 0
			self.ox_sem.release()
			self.hy_sem.release()
			self.hy_sem.release()


	def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
		self.hy_sem.acquire()
		releaseHydrogen()
		self.hyd += 1
		self.reset()


	def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
		self.ox_sem.acquire()
		releaseOxygen()
		self.oxy += 1
		self.reset()


if __name__ == "__main__":
	h2o = H2O()

	threads = []
	for i in range(0, 10):
		if i < 4:
			t = threading.Thread(group=None, target=h2o.oxygen, name="Thread ox", args=[h2o.relOxy])
		else:
			t = threading.Thread(group=None, target=h2o.hydrogen, name="Thread hy", args=[h2o.relHy])

		threads.append(t)
		t.start()
	