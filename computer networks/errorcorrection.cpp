#include <iostream>
#include <cmath>
#include <cstring>

using namespace std;

int main() {
    int i, j, k, count, err_pos = 0, flag = 0;
    char dw[20], cw[20], data[20];

    // Input data
    cout << "Enter data as binary bit stream (7 bits):" << endl;
    cin >> data;

    // Insert parity bits into data word
    for (i = 1, j = 0, k = 0; i < 12; i++) {
        if (i == pow(2, j)) {  // Insert parity bits
            dw[i] = '?';  // Placeholder for parity bit
            j++;
        } else {
            dw[i] = data[k];  // Insert actual data bits
            k++;
        }
    }

    // Calculate parity bits
    for (i = 0; i < 4; i++) {
        count = 0;
        for (j = pow(2, i); j < 12; j += 2 * pow(2, i)) {
            for (k = 0; k < pow(2, i); k++) {
                if (j + k < 12 && dw[j + k] == '1') {
                    count++;
                }
            }
        }
        // Assign parity bits based on even parity
        if (count % 2 == 0) {
            dw[(int)pow(2, i)] = '0';
        } else {
            dw[(int)pow(2, i)] = '1';
        }
    }

    // Display code word
    cout << "Code word is:" << endl;
    for (i = 1; i < 12; i++) {
        cout << dw[i];
    }
    cout << endl;

    // Input received Hamming code
    cout << "\nEnter the received Hamming code:" << endl;
    cin >> cw;

    // Move the received bits one position back to match parity bit indexing
    for (i = 12; i > 0; i--) {
        cw[i] = cw[i - 1];
    }

    // Check for errors in received code
    for (i = 0; i < 4; i++) {
        count = 0;
        for (j = pow(2, i); j < 12; j += 2 * pow(2, i)) {
            for (k = 0; k < pow(2, i); k++) {
                if (j + k < 12 && cw[j + k] == '1') {
                    count++;
                }
            }
        }
        if (count % 2 != 0) {
            err_pos += pow(2, i);  // Track error position
        }
    }

    if (err_pos == 0) {
        cout << "\nThere is no error in the received code word." << endl;
    } else {
        if (cw[err_pos] == dw[err_pos]) {
            cout << "\nThere are 2 or more errors in the received code." << endl;
            cout << "Sorry! Hamming code cannot correct 2 or more errors." << endl;
            flag = 1;
        } else {
            cout << "\nThere is an error in bit position " << err_pos << " of the received code word." << endl;
        }

        if (flag == 0) {
            // Correct the error
            cw[err_pos] = (cw[err_pos] == '1') ? '0' : '1';

            // Display the corrected code word
            cout << "\nCorrected code word is:" << endl;
            for (i = 1; i < 12; i++) {
                cout << cw[i];
            }
            cout << endl;
        }
    }

    return 0;
}
