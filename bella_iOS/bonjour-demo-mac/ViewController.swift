//
//  ViewController.swift
//  bonjour-demo-mac
//
//  Created by James Zaghini on 8/05/2015.
//  Copyright (c) 2015 James Zaghini. All rights reserved.
//

import Cocoa

class ViewController: NSViewController, NSTableViewDelegate, NSTableViewDataSource, BonjourServerDelegate {
    
    var bonjourServer: BonjourServer!
    
    @IBOutlet var tableView: NSTableView!
    @IBOutlet var toSendTextField: NSTextField!
    @IBOutlet var readLabel: NSTextField!
    @IBOutlet var sendButton: NSButton!
    
    @IBAction func sendData(_ sender: NSButton) {
        if let data = self.toSendTextField.stringValue.data(using: String.Encoding.utf8) {
            self.bonjourServer.send(data)
        }
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        self.bonjourServer = BonjourServer()
        self.bonjourServer.delegate = self
    }
    
    // MARK: Bonjour server delegates
    
    func didChangeServices() {
        self.tableView.reloadData()
    }
    
    func connected() {
        
    }
    
    func disconnected() {
        
    }
    
    func handleBody(_ body: NSString?) {
        self.readLabel.stringValue = body! as String
        if (self.readLabel.stringValue == "start"){
            print("legit")
        }
    }
    
    // MARK: TableView Delegates

    func numberOfRows(in aTableView: NSTableView) -> Int {
        return bonjourServer.devices.count
    }
    
    func tableView(_ tableView: NSTableView, objectValueFor tableColumn: NSTableColumn?, row: Int) -> Any?{
        var result = ""
        
        let columnIdentifier = tableColumn!.identifier
        if columnIdentifier == "bonjour-device" {
            let device = self.bonjourServer.devices[row]
            result = device.name
        }
        return result
    }
    
    func tableViewSelectionDidChange(_ notification: Notification) {
        print("notification: \(notification.userInfo)")

        if self.bonjourServer.devices.count > 0 {
            let service = self.bonjourServer.devices[self.tableView.selectedRow]
            self.bonjourServer.connectTo(service)
        }
    }
}
