# ai-math-agent
AI Agent using Openai LLM and Wolfram Alpha tool to solve math problems


```bash
> Entering new AgentExecutor chain...
To find the derivative of \(\cos(x)\), I need to use calculus rules. Specifically, I will use the standard derivative rule for trigonometric functions.

Action: wolfram_alpha
Action Input: derivative of cos(x)Assumption: d/dx(cos(x)) = -sin(x) 
Answer: d/dx(cos(x)) = -sin(x)I now know the final answer.

Final Answer: The derivative of \(\cos(x)\) is \(-\sin(x)\).

> Finished chain.
{'input': 'What is the derivative of cos(x)', 'output': 'The derivative of \\(\\cos(x)\\) is \\(-\\sin(x)\\).', 'intermediate_steps': [(AgentAction(tool='wolfram_alpha', tool_input='derivative of cos(x)', log='To find the derivative of \\(\\cos(x)\\), I need to use calculus rules. Specifically, I will use the standard derivative rule for trigonometric functions.\n\nAction: wolfram_alpha\nAction Input: derivative of cos(x)'), 'Assumption: d/dx(cos(x)) = -sin(x) \nAnswer: d/dx(cos(x)) = -sin(x)')]}
```
