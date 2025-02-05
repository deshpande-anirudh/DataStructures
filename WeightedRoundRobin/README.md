# Weighted Round Robin (WRR) - Probabilistic vs Deterministic

This repository provides implementations of **Weighted Round Robin (WRR)** in both **probabilistic** and **deterministic** forms. Weighted Round Robin is a scheduling algorithm used to distribute tasks or requests across multiple resources (e.g., servers, queues) based on assigned weights. Resources with higher weights receive more tasks than those with lower weights.

---

## Table of Contents
1. [Probabilistic Weighted Round Robin](#probabilistic-weighted-round-robin)
2. [Deterministic Weighted Round Robin](#deterministic-weighted-round-robin)
3. [Syntax of `random.choices()`](#syntax-of-randomchoices)
4. [Usage](#usage)
5. [Example](#example)
6. [Contributing](#contributing)
7. [License](#license)

---

## Probabilistic Weighted Round Robin

In the **probabilistic** approach, tasks are assigned to resources based on weights using a random selection process. This method relies on randomness to achieve the desired distribution over time.

### Key Characteristics:
- **Randomness**: Each selection is independent, and the distribution is probabilistic.
- **Short-Term Variability**: The distribution may not strictly follow the weights in the short term but approximates them over time.
- **Simplicity**: Easy to implement using Python's `random.choices()`.

### Implementation:
```python
import random

class ProbabilisticWRR:
    def __init__(self, resources):
        """
        Initialize the Probabilistic Weighted Round Robin scheduler.
        
        :param resources: A list of tuples where each tuple contains (resource_name, weight).
        """
        self.resources = [resource[0] for resource in resources]
        self.weights = [resource[1] for resource in resources]

    def get_next_resource(self):
        """
        Get the next resource based on weighted random selection.
        """
        return random.choices(self.resources, weights=self.weights, k=1)[0]
```

---

## Deterministic Weighted Round Robin

In the **deterministic** approach, tasks are assigned to resources in a predictable, repeating order based on their weights. This method ensures strict adherence to the weights in both the short and long term.

### Key Characteristics:
- **Predictability**: The order of resource selection is fixed and deterministic.
- **Strict Adherence**: The distribution of tasks matches the weights exactly.
- **Fairness**: Ensures no resource is starved or overloaded in the short term.

### Implementation:
```python
from collections import deque

class DeterministicWRR:
    def __init__(self, resources):
        """
        Initialize the Deterministic Weighted Round Robin scheduler.
        
        :param resources: A list of tuples where each tuple contains (resource_name, weight).
        """
        self.resources = deque()
        for resource, weight in resources:
            self.resources.extend([resource] * weight)

    def get_next_resource(self):
        """
        Get the next resource based on weighted round-robin selection.
        """
        resource = self.resources.popleft()
        self.resources.append(resource)  # Move the resource to the end of the queue
        return resource
```

---

## Syntax of `random.choices()`

The `random.choices()` function is used in the probabilistic implementation to select a resource based on weights. Here’s the syntax:

```python
random.choices(population, weights=None, *, cum_weights=None, k=1)
```

### Parameters:
- **`population`**: A list of elements to choose from (e.g., `['high', 'medium', 'low']`).
- **`weights`**: A list of weights corresponding to each element in the population (e.g., `[60, 30, 10]`).
- **`cum_weights`**: An alternative to `weights`, specifying cumulative weights.
- **`k`**: The number of elements to select (default is `1`).

### Example:
```python
import random

resources = ['high', 'medium', 'low']
weights = [60, 30, 10]

# Select one resource based on weights
selected_resource = random.choices(resources, weights=weights, k=1)[0]
print(selected_resource)  # Output: 'high' (60% chance), 'medium' (30% chance), or 'low' (10% chance)
```

---

## Usage

1. **Probabilistic WRR**:
   - Use this when randomness is acceptable, and you want a simple implementation.
   - Suitable for scenarios like load balancing where short-term variability is not critical.

2. **Deterministic WRR**:
   - Use this when strict adherence to weights is required.
   - Suitable for scenarios like task scheduling where predictability is important.

---

## Example

### Probabilistic WRR Example:
```python
resources = [('high', 60), ('medium', 30), ('low', 10)]
wrr = ProbabilisticWRR(resources)

for _ in range(10):
    print(wrr.get_next_resource())
```

### Deterministic WRR Example:
```python
resources = [('high', 60), ('medium', 30), ('low', 10)]
wrr = DeterministicWRR(resources)

for _ in range(10):
    print(wrr.get_next_resource())
```
