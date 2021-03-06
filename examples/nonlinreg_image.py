""" 
Estimates a linear warp field, between two images - 

The target is a "smile" the image is a frown and the goal is to estimate
the warp field between them.
    
The deformation is not manufactured by the spline model, and is a good
(realistic) test of the spline deformation model.
    
"""

from matplotlib.pyplot import imread

from imreg.models import model
from imreg.metrics import metric
from imreg.samplers import sampler

from imreg.visualize import plot
from imreg import register

# Form some test data (lena, lena rotated 20 degrees)
image = imread('data/frown.png')[:, :, 0]
template = imread('data/smile.png')[:, :, 0]

# Form the affine registration instance.
affine = register.Register(
    model.CubicSpline,
    metric.Residual,
    sampler.Spline
    )

# Coerce the image data into RegisterData.
image = register.RegisterData(image)
template = register.RegisterData(template)

# Smooth the template and image.
image.smooth(1.5)
template.smooth(1.5)

# Register.
step, search = affine.register(
    image,
    template,
    verbose=True
    )

plot.searchInspector(search)
