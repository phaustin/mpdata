"""Unit test for listing.py using numpy function for testing"""
from listings_zmianahalo import *
import numpy
import numpy.testing

knownValue = [[3,3,1,0.5,0.5,
               numpy.array([[0., 0, 0],
                            [0,  1, 0],
                            [0,  0, 0]]),
               numpy.array([[0.,  0,   0],
                            [0,   0.,  0.5],
                            [0,   0.5, 0]]),
               numpy.array([[0, 0,   0],
                            [0, 0.,  0.5],
                            [0, 0.5, 0]])],
              [3,3,1,0.5,0.5,
               numpy.array([[0., 0, 0],
                            [0,  0, 0],
                            [0,  0, 1]]),
               numpy.array([[0.,  0.,  0.5],
                            [0.,  0.,  0.],
                            [0.5, 0.,  0]]),
               numpy.array([[0,   0.,  0.5],
                            [0.,  0.,  0.],
                            [0.5, 0.,  0]])],
              [3,3,5,1.,0.,
               numpy.array([[0., 0, 0],
                            [0,  1, 0],
                            [0,  0, 0]]),
               numpy.array([[0.,  1., 0],
                            [0,   0., 0.],
                            [0,   0., 0]]),
               numpy.array([[0, 1,  0],
                            [0, 0., 0.],
                            [0, 0., 0]])],
               [3,3,4,0.,1.,
               numpy.array([[0., 0, 0],
                            [0,  1, 0],
                            [0,  0, 0]]),
               numpy.array([[0.,  0., 0],
                            [0,   0., 1.],
                            [0,   0., 0]]),
               numpy.array([[0, 0.,  0],
                            [0, 0., 1.],
                            [0, 0., 0]])]
                ]

def testMpdata(nx, ny, nt, cx, cy, n_iters, psi_in, psi_out):
    slv = Solver_2D(Mpdata, n_iters, Cyclic, Cyclic, nx, ny)
    slv.state()[:] = psi_in
    slv.Cx()[:] = cx
    slv.Cy()[:] = cy
    print "ind", slice(slv.i.start - 1, slv.i.stop),slv.j
    adwekcja = slv.adv
    print "slv.adv", adwekcja.n_halos
    #a_operator = a_op(0,slv.psi,slice(1, 5, None), slice(2, 5, None))
    slv.solve(nt)
    print "test dla parametrow: cx, cy, nt, n_iters", cx, cy, nt, n_iters
    print "psi rozw, roznica", slv.state(), slv.state() - psi_out
    print "test message: ", numpy.testing.assert_almost_equal(slv.state(), psi_out, decimal=5)


def test_aop(psi_in):
    pass
def main():
    for nx, ny, nt, cx, cy, psi_in, psi_out1, psi_out2 in knownValue:
        testMpdata(nx, ny, nt, cx, cy, 1, psi_in, psi_out1)
#        testMpdata(nx, ny, nt, cx, cy, 2, psi_in, psi_out2)
       
main()
