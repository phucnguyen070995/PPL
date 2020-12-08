#cau 1
    def visitIntLiteral(self, ast, o):
        return self.emit.emitPUSHCONST(ast.value, IntType(), o.frame), IntType()

        
#cau 2
    def visitFloatLiteral(self, ast, o):
        return self.emit.emitPUSHFCONST(str(ast.value), o.frame), FloatType()

#cau 3
    def visitBinExpr(self,ctx,o):
        frame = o.frame
        nenv = o.sym
        leftCode, typeLeft = self.visit(ctx.e1,  Access(frame, nenv, False, True))
        rightCode, typeRight = self.visit(ctx.e2,  Access(frame, nenv, False, True))
                
        op_str = leftCode + rightCode
        resType = typeRight
        if ctx.op in ['+','+.']: 
            op_str +=  self.emit.emitADDOP('+', resType, frame)
        elif ctx.op in ['-','-.']: 
            op_str +=  self.emit.emitADDOP('-', resType, frame)
        elif ctx.op in ['*', '*.']:
            op_str +=  self.emit.emitMULOP('*', resType, frame)
        elif ctx.op in ['/', '/.']:
            op_str +=  self.emit.emitDIV(frame)
        return op_str, resType

#cau 4
    def visitBinExpr(self,ctx,o):
        frame = o.frame
        nenv = o.sym
        leftCode, typeLeft = self.visit(ctx.e1,  Access(frame, nenv, False, True))
        rightCode, typeRight = self.visit(ctx.e2,  Access(frame, nenv, False, True))
        if type(typeLeft) != type(typeRight):
            if type(typeLeft) is IntType:
                leftCode += self.emit.emitI2F(frame)
                typeLeft = FloatType()
            elif type(typeRight) is IntType:
                rightCode += self.emit.emitI2F(frame)
                typeRight = FloatType()
        if ctx.op is '/':
            if type(typeLeft) is IntType:
                leftCode += self.emit.emitI2F(frame)
            if type(typeRight) is IntType:
                rightCode += self.emit.emitI2F(frame)
            
        op_str = leftCode + rightCode
        resType = typeRight
        if ctx.op in ['+', '-']: 
            op_str +=  self.emit.emitADDOP(ctx.op, resType, frame)
        elif ctx.op is '*':
            op_str +=  self.emit.emitMULOP('*', resType, frame)
        elif ctx.op is '/':
            resType = FloatType()
            op_str +=  self.emit.emitMULOP(ctx.op, resType, frame)

        elif ctx.op in ['==', '!=', '<', '<=', '>', '>='] :
            op_str += self.emit.emitREOP(ctx.op, resType, frame)
            resType = BoolType()
        return op_str, resType

#cau 5
    def visitId(self,ctx,o):
        symLst = []
        for x in o.sym:
            symLst+= [x]
        sym = self.lookup(ctx.name.lower(), symLst, lambda x: x.name.lower())
        if o.isLeft:
            if type(sym.value) is CName:
                return self.emit.emitPUTSTATIC(sym.value.value + "/" + sym.name,sym.mtype,o.frame), sym.mtype
            else:
                return self.emit.emitWRITEVAR(sym.name, sym.mtype, sym.value.value, o.frame), sym.mtype
        else:
            if type(sym.value) is CName:
                
                return self.emit.emitGETSTATIC(sym.value.value + "/" + sym.name,sym.mtype,o.frame), sym.mtype #load
            else:
                
                return self.emit.emitREADVAR(sym.name, sym.mtype, sym.value.value, o.frame), sym.mtype