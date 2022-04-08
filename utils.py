import pandas as pd
import pandas as pd
import plotly.express as px


def get_cores_num(cores):
    """Get how many cores to server have
    """
    return [f"core_{i}" for i in range(len(cores))]
    
    
def get_cores(cores):
    """Seperating the server cores in different column
    """
    
    cores_val = []
    for i in cores.split(","):
        try:
            cores_val.append(float(i.strip()))
        except:
            pass
    return cores_val
    
def convert_to_datetime(df):
    """Convert string to datetime.
    """
    df['datetime '] = pd.to_datetime(df['datetime '], format='%Y%m%d %H:%M:%S')
    return df

def preprocessing(df):
    """Preprocessing on dataframe
    """
    df = convert_to_datetime(df)
    df["cores"] = df["cores"].map(lambda x: get_cores(x))
    cores_num = get_cores_num(df["cores"].iloc[0])

    df[cores_num] = pd.DataFrame(df.cores.tolist())
    return df

def get_graph(df):
    """Getting the graph accoeding to the dataframe
    """
    to_plot = list(set(list(df.columns)) - set(["datetime ", "cores", "total", "buff/cache"]))
    print(to_plot)
    fig = px.line(df, x="datetime ", y=to_plot)
    return fig.to_html()

