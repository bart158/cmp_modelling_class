# -*- coding: utf-8 -*-
"""
Created on Tue May 28 15:36:49 2024

@author: norbert
"""

import numpy as np
import matplotlib.pyplot as plt

# Define the patterns for letters D, J, C, and M
D = np.array([
    [1, 1, 1, 1, 0],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 1, 0]
])

A = np.array([
    [0, 0, 1, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0],
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1]
])

C = np.array([
    [0, 1, 1, 1, 1],
    [1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [0, 1, 1, 1, 1]
])

M = np.array([
    [1, 0, 0, 0, 1],
    [1, 1, 0, 1, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1]
])

# Flatten the patterns and convert to bipolar form (-1 and 1)
patterns = [D, A, C, M]
patterns_flat = [pattern.flatten() * 2 - 1 for pattern in patterns]

# Function to plot patterns
def plot_patterns(patterns, title):
    fig, axes = plt.subplots(1, len(patterns), figsize=(12, 3))
    for i, pattern in enumerate(patterns):
        axes[i].imshow(pattern.reshape(7, 5), cmap='plasma')
        axes[i].axis('off')
    fig.suptitle(title)
    plt.show()

# Plot original patterns
plot_patterns(patterns_flat, 'Original Patterns')

# Initialize the weight matrix W
N = 7 * 5  # Number of neurons
W = np.zeros((N, N))

# Learning step: Calculate the weight matrix W
for p in patterns_flat:
    W += np.outer(p, p)

# Ensure no neuron has a self-connection
np.fill_diagonal(W, 0)

# Plot the weight matrix W
plt.imshow(W, cmap='gray')
plt.title('Weight Matrix W')
plt.colorbar()
plt.show()

# Update function using the sign function
def update_pattern(pattern, W, steps=5):
    for _ in range(steps):
        pattern = np.sign(W @ pattern)
    return pattern

# Check that memorized patterns remain unchanged
memorized_patterns = [update_pattern(p, W) for p in patterns_flat]
plot_patterns(memorized_patterns, 'Memorized Patterns After Update')

# Function to add noise by flipping n pixels
def add_noise(pattern, n):
    noisy_pattern = pattern.copy()
    flip_indices = np.random.choice(len(pattern), size=n, replace=False)
    noisy_pattern[flip_indices] *= -1
    return noisy_pattern

# Add noise to patterns
noisy_patterns = [add_noise(p, 10) for p in patterns_flat]
plot_patterns(noisy_patterns, 'Noisy Patterns')

# Recognize patterns
recognized_patterns = [update_pattern(p, W) for p in noisy_patterns]
plot_patterns(recognized_patterns, 'Recognized Patterns After Update')

# Function to determine if two patterns are the same
def patterns_match(p1, p2):
    return np.array_equal(p1, p2)

# Find the number of errors needed for hallucination
for flips in range(1, 36):
    hallucinated = False
    for pattern in patterns_flat:
        noisy_pattern = add_noise(pattern, flips)
        recognized_pattern = update_pattern(noisy_pattern, W)
        if not patterns_match(recognized_pattern, pattern):
            hallucinated = True
            break
    if hallucinated:
        print(f"Number of flips needed for hallucination: {flips}")
        break
