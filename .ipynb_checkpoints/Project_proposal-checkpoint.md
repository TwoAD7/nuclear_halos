{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h1><center>Gamma Ray Tracking</center></h1>\n",
    "\n",
    "<h4><center>By: Roy Salinas </center><h4>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<center> <img src=\"proposal_pic.jpg\" width=\"500\" height=\"500\" align=\"center\"/></center>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Image from: https://previews.123rf.com/images/generalfmv/generalfmv1312/generalfmv131200124/24660220-emission-of-a-gamma-ray-from-an-atomic-nucleus.jpg"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Overview\n",
    "----"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The study of nuclear matter is vital in gaining a better understanding of our universe as it pushes the frontier of our knowledge. Many phenomena encountered in nuclear physics is paramount to other fields of research such as condense matter and atomic physics due to the implicit dependence on structure and unique many body systems. One can pursue this endeavor by looking at lifetime measurements of excited states of nucleons, protons/neutrons, as they decay to lower energy states. In this decay process, energy is released in a discrete energy bundle known as a quanta - a.k.a. photon - while still being considered as a continuous electro-magnetic wave propagating through space. By measuring the energy of the emmitted photon, and through an analysis that concerns itself with the relativistic doppler shift, energy loss, insight from scientist, and a myriad of other facets, one can glean a better picture of the microscopic world in which quantum mechanics reigns.\n",
    "\n",
    "Due to the complex nature of this endeavor and the reality of funding, simulations have to be made to model such systems prior to executing such experiment. These models are configured with the physical aspects (detectors, limitations, target, beam,etc.) of the experiment one has planned and \"carried out\" via simulation. In this particular project, I will be utilizing the GEANT4Lifetime simulation program developed and used by the Lifetime group here at NSCL/FRIB. This simulation is designed to prepare and analyze experiements poised at measuring the lifetimes of nuclear states at NSCL/FRIB using the S800 spectrometer in combination with the gamma-ray spectrometer, SeGA or GRETINA. With this simulation available, I am aiming to create a neural network/machine learning model to identify compton scattered events and pair production events from interactions of our incoming particle beam and target. From there, I will compare the efficiency of this method to the traditional method of using the compton scattering formula, pattern of hits formula and usual assumptions made about our system.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Program Description \n",
    "---"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "At this stage, I am not sure in which direction I will go; either python or ROOT. If I were to take the python path, I will have the breadth of pytorch, scikit-learn, TensorFlow, etc. available to me and will have this to my advantage. However, if I were to go with ROOT, which is a c++ framework, I will have access to the TookKit for MultiVariate Analysis (TMVA) to work with. I am not sure as to which one is more advantageous to me at the moment but what is for certain is that I will be using a machine learning method/neural network to create a regression model for compton scattered events and pair production events.\n",
    "\n",
    "The aim is to generate data with the GEANT4Lifetime simulation that contains both compton scattered and pair produced events and train my model on a set of training data. From there, I will test it with a set of testing data and continue optimizing (neuron type, learning parameter, propagation method, etc.) until I have reached a model that best matches the test data. Once that is completed, I aim to compare this model with the traditional approach mentioned in the second paragraph of \"Overview\". This will serve as a direct comparison of how modern adavancements in computing algorithms do when contrasted with the analytical solution and assumptions based on the physics. Ultimately, it will serve as a \"double check\" that the machine learning method is reproducing the physics we want and that the results are the same, regardless of the approach taken."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Project Goals and Timeline\n",
    "---"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### **Goals**\n",
    "\n",
    "#### Long term\n",
    " * Gain a better understanding on the physics of nuclear structure and dynamics\n",
    " * Improve coding abilities \n",
    " * Gain a better understanding of machine learnin/neural networks \n",
    "     * Includes specific details about different librairies and advantages to different kind of problems\n",
    " * Work on applying computational methods to the field of nuclear physics \n",
    "     \n",
    "#### Short term\n",
    " * __Surive my first year as a graduate student__ \n",
    " * Pass this class\n",
    " * Get model working for analysis\n",
    "\n",
    "### **Timeline**\n",
    " * 09/30/2020 - 10/03/2020: Install Geant4Lifetime software and understand in and outs\n",
    " * 10/05/2020 - 10/17/2020: Work on developing neural network and read on literature on physics aspect and machine learning aspect \n",
    " * 10/17/2020 - 10/31/2020: Testing and optimizing model\n",
    " * 11/01/2020 - 11/15/2020: More testing and optimizing \n",
    " * 11/15/2020 - 11/20/2020: Have rudimentary comparison between traditional approach and machine learning/neural network approach \n",
    " * 12/20/2020 - 12/09/2020: Work on presentation and debugging final details\n",
    " \n",
    "The timeline listed above is very generous as I am not sure how my other classes and my TA'ing responsibilities will change as the semester progresses. "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Anticipating challenges \n",
    "---"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## <u>Physics Facet</u>\n",
    " * Need to read more literature about nuclear structure and dynamics\n",
    "     * Nuclear shell model \n",
    "     * Excitation of nucleons in nuclei \n",
    " * What has been done with gamma ray tracking as of now\n",
    "     * Implemented methods (has machine learning been applied to this kind of physiscs?)\n",
    "     \n",
    "## <u>Computational Facet</u>\n",
    " * Go over different modules in python\n",
    " * Decide over TMVA or python neural net. modules \n",
    " * Structure of neural network\n",
    "     * How will I create and handle the data strctures and objects required for this?\n",
    " * Decided if I want to run this on my machine or HCPP\n",
    "     * Most likely HCPP (need to figure that out) \n",
    "     \n",
    "## <u>General Worries</u>\n",
    " * Other classes course load \n",
    " * TA'ing responsibility \n",
    " * Mental sanity \n",
    " \n",
    " \n",
    "If any challenges interfere with my ability to complete my project or progress, there will be some scaling down of the over arching goal of the project to have successful deliverable at the end this semester. This project may deviate from the python intended goal due to having equal amounts of experience with scki-kit learn and TMVA but not PyTorch, TensorFlow, etc. That may be the only deviation."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
