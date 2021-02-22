import numpy as np
import random


class Generator:
    # 0 means empty field, 1 me, 2 enemy
    # array length of each dataset is 10, 9 fields, one result field, between 0-2, 0 nobody won, 1 me, 2 enemy
    # If first_turn is zero, the first turn will be randomly chosen
    def __init__(self, datasetSize, first_turn=1):
        assert datasetSize != 0
        assert first_turn is not None
        assert first_turn == 1 or first_turn == -1 or first_turn == 2

        self.first_turn = first_turn
        self.data = np.zeros([datasetSize, 10])

        if self.first_turn == 1:
            self.max1 = 5
            self.max2 = 4
        elif self.first_turn == 2:
            self.max1 = 4
            self.max2 = 5

    # generate will return a numpty object.
    def generate(self):
        for count in range(len(self.data)):
            element = self.data[count]

            if self.first_turn == -1:
                self.max1 = random.randint(4, 5)
                self.max2 = 9 - self.max1

            max1tmp = 0  # Not allowed -1
            max2tmp = 0

            for count2 in range(len(element) - 1):
                x = random.randint(0, 2)

                if x == 1:
                    if max1tmp == -1:
                        if max2tmp != -1:
                            x = 2

                            max2tmp = max2tmp + 1

                            if max2tmp == self.max2:
                                max2tmp = -1
                        else:
                            x = 0
                    else:
                        max1tmp = max1tmp + 1

                        if max1tmp == self.max1:
                            max1tmp = -1
                elif x == 2:
                    if max2tmp == -1:
                        if max1tmp != -1:
                            x = 1

                            max1tmp = max1tmp + 1

                            if max1tmp == self.max1:
                                max1tmp = -1
                        else:
                            x = 0
                    else:
                        max2tmp = max2tmp + 1

                        if max2tmp == self.max2:
                            max2tmp = -1

                element[count2] = x

                if self.checkWhoWon(element) != 0:
                    continue

            element[9] = self.checkWhoWon(element)

        return self.data

    def checkWhoWon(self, dataset):
        assert dataset is not None
        assert len(dataset) >= 9

        # Horizontal
        if dataset[0] == dataset[1] and dataset[1] == dataset[2] and dataset[0] != 0:
            return dataset[0]
        elif dataset[3] == dataset[4] and dataset[4] == dataset[5] and dataset[3] != 0:
            return dataset[3]
        elif dataset[6] == dataset[7] and dataset[7] == dataset[8] and dataset[6] != 0:
            return dataset[6]

        # Vertical
        elif dataset[0] == dataset[3] and dataset[3] == dataset[6] and dataset[0] != 0:
            return dataset[0]
        elif dataset[1] == dataset[4] and dataset[4] == dataset[7] and dataset[1] != 0:
            return dataset[1]
        elif dataset[2] == dataset[5] and dataset[5] == dataset[8] and dataset[2] != 0:
            return dataset[2]

        # Diagonal
        elif dataset[6] == dataset[4] and dataset[4] == dataset[2] and dataset[6] != 0:
            return dataset[6]
        elif dataset[0] == dataset[4] and dataset[4] == dataset[8] and dataset[0] != 0:
            return dataset[0]
        else:
            return 0
