import random
import solara
import tiktoken

tokenizer = tiktoken.encoding_for_model("gpt-4")
text1 = solara.reactive("Example text is here")
text2 = solara.reactive("")
@solara.component
def Page():
  solara.Markdown("#GPT token encoder and decoder")
  solara.InputText("Enter text to tokenize it:", value=text1, continuous_update=True)
  tokens = tokenizer.encode(text1.value)
  spans = ""
  spans1 = ""
  for i, token in enumerate(tokens):
    random.seed(i)
    random_color = ''.join([random.choice('0123456789ABCDEF') for k in range(6)])
    spans += " " + f"<span style='font-family: cursive;color: #{random_color}'>{token}</span>"
    spans1 += " " + f"""<span style="
        padding: 5px;
        border-right: 3px solid white;
        line-height: 3em;
        font-family: courier;
        background-color: #{random_color};
        color: white;
        position: relative;
      "><span style="position: absolute; top: 5.5ch; line-height: 1em; left: -0.5px; font-size: 0.45em">{token}</span>{tokenizer.decode([token])}</span>"""
  solara.Markdown(f"{spans}")
  solara.Markdown(f"{len(tokens)} token") if len(tokens)==1 else solara.Markdown(f"{len(tokens)} tokens")
  solara.Markdown(f'{spans1}')
  solara.InputText("Or convert space separated tokens to text:", value=text2, continuous_update=True)
  spans2 = text2.value.split(' ')
  spans2 = [int(span) for span in spans2 if span != ""]
  spans2 = tokenizer.decode(spans2)
  solara.Markdown(f'{spans2}')

Page()
