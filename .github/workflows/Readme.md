Adding Custom Configuration Fields (Inputs)
To fine-tune your math parameters 
(e.g.: testing a different value for \alpha^{-1} or \delta_{\text{shear}}) directly from the GitHub UI without modifying the Python script every time, expand the workflow_dispatch block to accept custom text or dropdown inputs.
Here is how to configure it to add interactive text boxes to the "Run workflow" button:


on:
  workflow_dispatch:
    inputs:
      alpha_inv:
        description: 'Global Foliation Resonance Scale (Inverse Alpha)'
        required: true
        default: '137.0354'
      delta_shear:
        description: 'Geometric Torsional Shear Boundary Limit'
        required: true
        default: '0.681690'
        
