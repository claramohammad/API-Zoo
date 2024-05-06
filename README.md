# API Zoológico

#### Sobre o Projeto

Este projeto é uma simulação de API para um zoológico, projetado para facilitar a gestão de animais, recintos e visitantes. O sistema é desenvolvido em Python e utiliza princípios de programação orientada a objetos para modelar a lógica de negócios do zoológico. Ele foi criado com o objetivo de demonstrar a aplicação de conceitos básicos de programação, estruturas de dados e interações entre objetos.

#### Funcionalidades Principais

**Criação de Animais:** Permite a criação de animais com atributos como nome, espécie e nível de felicidade.

**Criação de Recintos:** Suporta a criação de recintos para animais da mesma espécie, permitindo também a alteração dos animais nesses recintos.

**Alimentação de Animais:** Funcionalidade para alimentar animais, impactando diretamente seu nível de felicidade.

**Gestão de Visitantes:** A API calcula a receita gerada a partir do número de visitantes, que é influenciada pela felicidade dos animais e pelo estado dos recintos.

#### Estrutura do Projeto

O projeto é estruturado em três classes principais:

**Classe Animal:** Representa os animais no zoológico. Cada animal possui um nome, uma espécie e um atributo de felicidade.

**Classe Enclosure:** Agrupa animais da mesma espécie.

**Classe Zoo:** Age como um contêiner para múltiplos recintos e gerencia a interação com visitantes, calculando receitas com base nas condições do zoológico.

#### Testes Unitários

Utilizando a metodologia TDD (Desenvolvimento Orientado por Testes), o projeto inclui uma série de testes unitários que garantem a funcionalidade e robustez das operações oferecidas pela API. Estes testes são fundamentais para assegurar que as interações entre as classes e métodos estão produzindo os resultados esperados.
