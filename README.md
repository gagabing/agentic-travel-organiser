# Travel Planner

A Jupyter notebook that uses LangGraph to research a destination and create a
reviewable, day-by-day travel itinerary. The notebook asks for trip details,
researches interests, schedules activities, and writes an HTML travel plan.

## Requirements

- Python 3.13 or newer
- An OpenAI API key
- A Tavily API key
- A notebook environment, such as VS Code with the Jupyter extension or JupyterLab

## Set up the API keys

From the repository root, copy `.env.example` to `.env` and add your keys:

```dotenv
OPENAI_API_KEY=your-openai-api-key
TAVILY_API_KEY=your-tavily-api-key
```

The notebook loads these values from `.env`. OpenAI is used for the language
model, and Tavily is used for web search. Both services may incur usage charges
according to your account plans. Keep `.env` private; it is excluded from Git.
The LangSmith variables in `.env.example` are optional and are not required to
run the notebook.

## Install with uv

Install [uv](https://docs.astral.sh/uv/), then run these commands from the
repository root:

```bash
uv sync
uv run --with jupyterlab jupyter lab
```

`uv sync` creates the project environment and installs the pinned dependencies
from `uv.lock`. The second command launches JupyterLab, adding it for this run
without changing the project dependencies. Alternatively, open
`travel_agent.ipynb` in VS Code with the Jupyter extension and select the
project's `.venv` interpreter.

## Install with pip

Create and activate a virtual environment from the repository root, then
install the dependencies:

```bash
python -m venv .venv
```

On Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

On macOS or Linux:

```bash
source .venv/bin/activate
```

Then install the dependencies and, if you want to run JupyterLab locally, the
notebook interface:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip install jupyterlab
python -m jupyter lab
```

You can omit the last two commands if you use VS Code with the Jupyter
extension. Select the virtual environment you created as the notebook's Python
kernel.

## Run the notebook

Open `travel_agent.ipynb` from the repository root, select the environment you
set up, and run the cells in order. Keep the `travel_agent_support` directory
next to the notebook; it contains helper code used by the notebook.

## Output

Running the final notebook cell generates `travel_plan.html` in the repository
root. It is a useful, shareable artefact of a particular notebook run, rather
than source code; commit it when you want to include that example plan, and
regenerate it when the itinerary or notebook changes.
