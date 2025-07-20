import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.io as pio

# Set default renderer for environments (uncomment one that fits your case)
# pio.renderers.default = 'browser'       # Opens in browser
# pio.renderers.default = 'notebook'      # For Jupyter Notebook
# pio.renderers.default = 'colab'         # For Google Colab
# pio.renderers.default = 'vscode'        # If using VS Code Jupyter

# Sample data
data = {
    "Age": [23, 45, 31, 35, 40, 29, 34, 35, 22, 45, 32, 27, 50, 33, 31, 22, 31, 29, 26, 48, 41, 35, 39, 24],
    "Gender": [
        "Male", "Female", "Female", "Male", "Male", "Female", "Male", "Male", "Female", "Female",
        "Male", "Female", "Male", "Female", "Male", "Female", "Female", "Male", "Female", "Male",
        "Male", "Female", "Female", "Male"
    ]
}
df = pd.DataFrame(data)

# Create subplot layout: 1 row, 2 columns
fig = make_subplots(rows=1, cols=2, subplot_titles=("Gender Distribution", "Age Distribution"))

# Gender distribution bar chart
gender_counts = df['Gender'].value_counts()
fig.add_trace(
    go.Bar(
        x=gender_counts.index,
        y=gender_counts.values,
        marker_color=['#1FB8CD', '#FFC185'],
        name="Gender"
    ),
    row=1, col=1
)

# Age histogram
fig.add_trace(
    go.Histogram(
        x=df['Age'],
        nbinsx=10,
        marker_color='#A593E0',
        name="Age"
    ),
    row=1, col=2
)

# Layout updates
fig.update_layout(
    title_text="Population Distribution by Gender and Age",
    bargap=0.2,
    showlegend=False,
    height=500,
    width=900
)

fig.update_xaxes(title_text="Gender", row=1, col=1)
fig.update_yaxes(title_text="Count", row=1, col=1)
fig.update_xaxes(title_text="Age", row=1, col=2)
fig.update_yaxes(title_text="Frequency", row=1, col=2)

# Show the plot
fig.show()

# Save as HTML (open manually if show() fails)
fig.write_html("population_distribution.html")

# Optional: Save as image (requires `pip install kaleido`)
# fig.write_image("population_distribution.png")
