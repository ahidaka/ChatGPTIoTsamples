# Adjusting the X-axis starting position to ensure no overlap between the y-axes and the graph

# Plotting with updated colors and axis position for Humidity
fig, ax1 = plt.subplots(figsize=(15, 8))

# Adjust the position to avoid overlap
fig.subplots_adjust(left=0.20)

# Humidity
ax2 = ax1.twinx()
line2, = ax2.plot(summary_df['Hour'], summary_df['Humidity'], color='aqua', label='Humidity (%)')
ax2.set_ylabel('Humidity (%)', color='aqua')
ax2.set_ylim(0, 100)
ax2.tick_params(axis='y', labelcolor='aqua')
ax2.yaxis.set_label_position("left")
ax2.yaxis.tick_left()
ax2.spines['left'].set_position(('outward', 40))

# Temperature
line1, = ax1.plot(summary_df['Hour'], summary_df['Temperature'], color='deeppink', label='Temperature (Åé)')
ax1.set_xlabel('Hour')
ax1.set_ylabel('Temperature (Åé)', color='deeppink')
ax1.set_ylim(0, 50)
ax1.tick_params(axis='y', labelcolor='deeppink')

# Illuminance
ax3 = ax1.twinx()
ax3.spines['right'].set_position(('outward', 60))
line3, = ax3.plot(summary_df['Hour'], summary_df['Illuminance'], color='brown', label='Illuminance (lx)')
ax3.set_ylabel('Illuminance (lx)', color='brown')
ax3.set_ylim(0, 100)
ax3.tick_params(axis='y', labelcolor='brown')

# Signal Strength
ax4 = ax1.twinx()
ax4.spines['right'].set_position(('outward', 120))
line4, = ax4.plot(summary_df['Hour'], summary_df['Signal Strength'], color='lightgreen', label='Signal Strength (dbm)')
ax4.set_ylabel('Signal Strength (dbm)', color='lightgreen')
ax4.set_ylim(-100, -50)
ax4.tick_params(axis='y', labelcolor='lightgreen')

# Legend
ax1.legend(handles=[line1, line2, line3, line4], loc='upper left', frameon=True)

# Title and show
plt.title('Hourly Averages of Telemetry Data')
fig.tight_layout()
plt.show()
