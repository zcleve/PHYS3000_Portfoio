import numpy as np
import matplotlib.pyplot as plt
from scipy import signal


# Generate a noisy sine wave signal
np.random.seed(0)  # for reproducibility
t = np.linspace(0, 1, 1000, endpoint=False)  # time axis
f_signal = 5  # frequency of the sine wave
signal_noisy = np.sin(2 * np.pi * f_signal * t) + 0.5 * np.random.randn(len(t))  # noisy sine wave

# Define the low-pass filter
f_cutoff = 8  # cutoff frequency
nyquist = 0.5 * 1000  # Nyquist frequency for the sampling rate of 1000 Hz
order = 5  # order of the filter
b, a = signal.butter(order, f_cutoff / nyquist, 'low')  # Butterworth low-pass filter coefficients

# Apply the low-pass filter to the noisy signal
signal_filtered = signal.filtfilt(b, a, signal_noisy)

# Plot the original noisy signal and the filtered signal
plt.figure(figsize=(10, 6))

# Original noisy signal
plt.subplot(2, 1, 1)
plt.plot(t, signal_noisy, label='Noisy Signal')
plt.title('Original Noisy Signal (Before Filtering)')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend()

# Filtered signal
plt.subplot(2, 1, 2)
plt.plot(t, signal_filtered, label='Filtered Signal', color='orange')
plt.title('Filtered Signal (After Low-Pass Filtering)')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend()

plt.tight_layout()
plt.show()