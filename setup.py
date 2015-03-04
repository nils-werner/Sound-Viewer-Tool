from setuptools import setup

setup(
    name='svt',
    version='1.1',
    author='Luis J. Villanueva',
    author_email='coquipr.com@gmail.com',
    url='https://github.com/ljvillanueva/Sound-Viewer-Tool',

    description='Generate waveform and spectrogram png images from a wav file',
    long_description='This Python script uses the numpy and audiolab modules to generate waveform and spectrogram png images from a wav file. It is based on a script by Freesound.org.',

    install_requires=[
        'numpy>=1.1',
        'scikits.audiolab>=0.8',
        'Pillow',
    ],

    platforms='any',
    keywords=['audio'],
    license='GPL3',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Topic :: Multimedia :: Sound/Audio'
    ],
    scripts=['svt.py'],
)
