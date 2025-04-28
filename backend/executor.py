import matplotlib.pyplot as plt
import plotly.io as pio
import base64
import io

def safe_execute(code, dataframes):
    local_vars = {"dataframes": dataframes}
    
    try:
        exec(code, {}, local_vars)
        answer = local_vars.get('answer', "No answer generated.")

        img_base64 = None

        # Check for Matplotlib figures
        img_buf = io.BytesIO()
        if plt.get_fignums():
            plt.savefig(img_buf, format='png')
            plt.close()
            img_buf.seek(0)
            img_base64 = base64.b64encode(img_buf.read()).decode('utf-8')

        # Check for Plotly figures
        elif 'fig' in local_vars:
            fig = local_vars['fig']
            if fig:
                img_buf = io.BytesIO()
                fig.write_image(img_buf, format='png')
                img_buf.seek(0)
                img_base64 = base64.b64encode(img_buf.read()).decode('utf-8')

        return {
            "answer": answer,
            "graph": img_base64
        }
    except Exception as e:
        return {"error": str(e)}
