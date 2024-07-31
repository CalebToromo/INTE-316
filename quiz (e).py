import numpy as np
import matplotlib.pyplot as plt

# Define the signal parameters
f1 = 50  # frequency in Hz
f2 = 120  # frequency in Hz
sampling_rate = 1000  # samples per second
duration = 1  # in seconds

# Time array
t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)

# Signal s(t)
s = np.sin(2 * np.pi * f1 * t) + np.sin(2 * np.pi * f2 * t)

# Compute the FFT
fft_result = np.fft.fft(s)
fft_freqs = np.fft.fftfreq(len(fft_result), 1 / sampling_rate)

# Only take the positive half of the spectrum
positive_freqs = fft_freqs[:len(fft_freqs) // 2]
positive_fft = np.abs(fft_result[:len(fft_result) // 2])

# Plot the signal and its frequency spectrum
plt.figure(figsize=(14, 6))

plt.subplot(2, 1, 1)
plt.plot(t, s)
plt.title('Signal in Time Domain')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.subplot(2, 1, 2)
plt.plot(positive_freqs, positive_fft)
plt.title('Frequency Domain')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.grid()

plt.tight_layout()
plt.show()
s