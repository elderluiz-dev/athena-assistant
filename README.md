# Athena Assistant
Athena é uma assistente pessoal inteligente, modular e prioritariamente offline, desenvolvida em Python para Linux. Sua finalidade é oferecer uma interface de interação por voz entre o usuário e o computador, permitindo monitoramento, consultas, execução de comandos e gerenciamento de tarefas.

# Motivação
A Athena foi primeiramente idealizada pela falta de um assistente pessoal SEM IA, desprendendo da ideia de uma IA autônoma com processamento próprio de tarefas. A Athena usa de uma lista pré definida de comandos bem estruturados que promovem um grande ganho de eficiência em tarefas simples em comparação com assistentes de IA que utilizam de processamento de tokens, gastando dinheiro ou processamento.

# Limitações
Justamente por ser uma assistente que não utiliza de modelos de linguagem para processamento de tarefas, a Athena possui uma quantidade limitade de funções, sendo restrira apenas à aquelas colocadas no código.

# Estrutura

```
.
├── core
│   ├── interface.py
│   └── modules
│       ├── system_monitor.py
│       └── time.py
├── docs
│   └── 01-flow.png
├── main.py
└── README.md
```

---
Versão atual: v0.1 || Fase: Prototipação  em terminal