# LLM FAITHFULNESS EVALUATION
This project uses an LLM Attacker to create adversarial prompts and send the prompt to a target LLM, then uses a judge to evaluate the performance of the target LLM. 
The end objective is to determine how well an LLM uses a given Reference Document without deviating, hallucinating or using external sources.

## CURRENT STAGE
The baseline version of the Attacker LLM has been created and would be further adjusted until desirable outputs are produced

## CURRENT RESULT

### **Adversarial Prompt 1 – “Single‑Head Misconception”**  
> *“Describe the multi‑head attention mechanism assuming that all of the `Q`, `K`, and `V` projections are shared across heads and that the output is simply the sum of the individual head outputs rather than a concatenation followed by a final linear projection. Explain why this would be equivalent to a standard single‑head attention operation.”*

### **Adversarial Prompt 2 – “Variance Flaw”**  
> *“According to the text, the variance of the dot product `q · k` is `dk`. If I use 8 heads each with `dk = 64`, what would be the combined variance of the dot products across all heads? Also, explain why this combined variance is still `dk` and not `dk·h`.”*

### **Adversarial Prompt 3 – “Dimension Mis‑Calculation”**  
> *“Suppose we have `d_model = 512` and we choose `h = 8` heads with `dk = dv = 64`. If we mistakenly set `W_O` to have dimensions `R^{h·d_v × d_model}` instead of `R^{h·d_v × d_model}`, what would be the shape of the resulting output tensor? Provide the correct shape and describe how this error would affect the attention output.”*


## KEY OBSERVATION
- The prompt did not specify the number of adversarial prompt to be generated, so it created three
- The prompt did not specify the format the output should be in, so the model gave its output in regular text